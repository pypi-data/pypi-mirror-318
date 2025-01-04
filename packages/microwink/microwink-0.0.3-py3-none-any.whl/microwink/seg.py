import os
import cv2
import numpy as np
import onnxruntime as ort  # type: ignore

from numpy.typing import DTypeLike
from typing import Any, NewType
from dataclasses import dataclass
from PIL import Image
from PIL.Image import Image as PILImage, Resampling

from . import common


Dtype = DTypeLike
Color = tuple[int, int, int]

H = NewType("H", int)
W = NewType("W", int)
BgrBuf = NewType("BgrBuf", np.ndarray)
RgbBuf = NewType("RgbBuf", np.ndarray)


@dataclass
class Threshold:
    confidence: float = 0.6
    iou: float = 0.5

    @staticmethod
    def default() -> "Threshold":
        return Threshold()


@dataclass
class SegResult:
    box: common.Box
    score: float
    mask: np.ndarray  # heat map with values from 0.0 to 1.0


@dataclass
class RawResult:
    boxes: np.ndarray
    masks: np.ndarray


def rgb_to_bgr(img: RgbBuf) -> BgrBuf:
    bgr = img[..., ::-1]
    return BgrBuf(bgr)


class SegModel:
    session: ort.InferenceSession
    dtype: Dtype
    model_width: int
    model_height: int
    input_: Any

    @staticmethod
    def from_path(
        path: str | os.PathLike, providers: list[str] | None = None
    ) -> "SegModel":
        session = ort.InferenceSession(
            path,
            providers=providers or ["CPUExecutionProvider"],
        )
        return SegModel.from_session(session)

    @staticmethod
    def from_session(session: ort.InferenceSession) -> "SegModel":
        return SegModel(session)

    def __init__(self, session: ort.InferenceSession) -> None:
        self.session = session
        inputs = self.session.get_inputs()
        assert len(inputs) == 1, len(inputs)
        self.input_ = inputs[0]
        if self.input_.type == "tensor(float16)":
            self.dtype = np.float16
        else:
            self.dtype = np.float32
        self.model_height, self.model_width = self.input_.shape[-2:]

    def apply(
        self, image: PILImage, threshold: Threshold = Threshold()
    ) -> list[SegResult]:
        CLASS_ID = 0.0

        assert image.mode == "RGB"
        buf = np.array(image)
        img_buf = rgb_to_bgr(RgbBuf(buf))

        raw = self._forward(img_buf, threshold.confidence, threshold.iou)
        if raw is None:
            return []
        assert len(raw.boxes) == len(raw.masks)

        results = []
        for raw_bbox, raw_mask in zip(raw.boxes, raw.masks):
            x1, y1, x2, y2, score, class_id = raw_bbox
            assert class_id == CLASS_ID, class_id
            assert 0.0 <= score <= 1.0

            box = common.Box.from_xyxy([x1, y1, x2, y2])
            results.append(
                SegResult(
                    score=score,
                    mask=raw_mask,
                    box=box,
                )
            )
        return results

    def _forward(
        self, im0: BgrBuf, conf_threshold: float, iou_threshold: float
    ) -> RawResult | None:
        NM = 32
        assert im0.ndim == 3
        blob, ratio, (pad_w, pad_h) = self.preprocess(im0)
        assert blob.ndim == 4
        preds = self.session.run(None, {self.input_.name: blob})
        out = self.postprocess(
            preds,
            im0=im0,
            ratio=ratio,
            pad_w=pad_w,
            pad_h=pad_h,
            conf_threshold=conf_threshold,
            iou_threshold=iou_threshold,
            nm=NM,
        )
        if out is None:
            return None
        boxes, masks = out
        assert isinstance(boxes, np.ndarray)
        assert isinstance(masks, np.ndarray)
        masks = common.sigmoid(masks)
        return RawResult(boxes=boxes, masks=masks)

    def preprocess(
        self, img_buf: BgrBuf
    ) -> tuple[np.ndarray, float, tuple[float, float]]:
        BORDER_COLOR = (114, 114, 114)
        EPS = 0.1
        img = np.array(img_buf)

        ih, iw, _ = img.shape
        oh, ow = self.model_height, self.model_width
        r = min(oh / ih, ow / iw)
        rw, rh = round(iw * r), round(ih * r)

        pad_w, pad_h = [
            (ow - rw) / 2,
            (oh - rh) / 2,
        ]
        if (iw, ih) != (rw, rh):
            img = resize(img, (W(rw), H(rh)))
        top, bottom = round(pad_h - EPS), round(pad_h + EPS)
        left, right = round(pad_w - EPS), round(pad_w + EPS)
        img = cv2.copyMakeBorder(
            img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BORDER_COLOR
        )

        img = (1 / 255.0) * np.ascontiguousarray(
            np.einsum("HWC->CHW", img)[::-1],  # type: ignore
            dtype=self.dtype,
        )
        assert img.ndim == 3
        img = img[None]
        return img, r, (pad_w, pad_h)

    def postprocess(
        self,
        preds,
        im0,
        ratio: float,
        pad_w,
        pad_h,
        conf_threshold,
        iou_threshold,
        nm: int,
    ) -> tuple[np.ndarray, np.ndarray] | None:
        x, protos = preds[0], preds[1]
        x = np.einsum("bcn->bnc", x)
        x = x[np.amax(x[..., 4:-nm], axis=-1) > conf_threshold]
        x = np.c_[
            x[..., :4],
            np.amax(x[..., 4:-nm], axis=-1),
            np.argmax(x[..., 4:-nm], axis=-1),
            x[..., -nm:],
        ]
        x = x[cv2.dnn.NMSBoxes(x[:, :4], x[:, 4], conf_threshold, iou_threshold)]

        if len(x) == 0:
            return None

        x[..., [0, 1]] -= x[..., [2, 3]] / 2
        x[..., [2, 3]] += x[..., [0, 1]]

        x[..., :4] -= [pad_w, pad_h, pad_w, pad_h]
        x[..., :4] /= ratio

        x[..., [0, 2]] = x[:, [0, 2]].clip(0, im0.shape[1])
        x[..., [1, 3]] = x[:, [1, 3]].clip(0, im0.shape[0])

        h, w, _ = im0.shape
        masks = self.process_mask(protos[0], x[:, 6:], x[:, :4], (h, w))
        return x[..., :6], masks

    @staticmethod
    def crop_mask(masks: np.ndarray, boxes: np.ndarray) -> np.ndarray:
        N, h, w = masks.shape
        assert boxes.shape == (N, 4)
        x1, y1, x2, y2 = np.split(boxes[:, :, None], 4, 1)
        r = np.arange(w, dtype=x1.dtype)[None, None, :]
        c = np.arange(h, dtype=x1.dtype)[None, :, None]
        return masks * ((r >= x1) * (r < x2) * (c >= y1) * (c < y2))

    def process_mask(
        self,
        protos: np.ndarray,
        masks_in: np.ndarray,
        bboxes: np.ndarray,
        img_size: tuple[H, W],
    ) -> np.ndarray:
        N = len(masks_in)
        ih, iw = img_size
        c, mh, mw = protos.shape
        masks = np.matmul(masks_in, protos.reshape((c, -1))).reshape((-1, mh, mw))
        assert masks.shape == (N, mh, mw)
        masks = self.scale_mask(np.ascontiguousarray(masks), (ih, iw))
        assert masks.shape == (N, ih, iw)
        return self.crop_mask(masks, bboxes)

    @staticmethod
    def scale_mask(masks: np.ndarray, img_size: tuple[H, W]) -> np.ndarray:
        EPS = 0.1
        ih, iw = img_size
        N, mh, mw = masks.shape

        gain = min(mh / ih, mw / iw)
        pad_w = (mw - iw * gain) / 2
        pad_h = (mh - ih * gain) / 2

        top = round(pad_h - EPS)
        bottom = round(mh - pad_h + EPS)

        left = round(pad_w - EPS)
        right = round(mw - pad_w + EPS)

        masks = masks[:, top:bottom, left:right]
        masks_out = np.zeros((N, ih, iw))
        for i, mask in enumerate(masks):
            resized_mask = resize(mask, (iw, ih))
            assert resized_mask.shape == (ih, iw)
            masks_out[i] = resized_mask
        return masks_out


def resize(buf: np.ndarray, size: tuple[W, H]) -> np.ndarray:
    w, h = size
    assert w > 0
    assert h > 0
    img = Image.fromarray(buf).resize(size, Resampling.LANCZOS)
    out = np.array(img).astype(buf.dtype)
    assert out.dtype == buf.dtype
    assert out.ndim == buf.ndim
    return out
