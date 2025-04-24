import cv2
import numpy as np
from PIL import Image
from typing import Union
from ..exceptions import FrameEncodeError

class Frame:
    def __init__(self, frame: Union[Image.Image, np.ndarray]):
        if isinstance(frame, Image.Image):
            self._data = np.array(frame)
        elif isinstance(frame, np.ndarray):
            if frame.ndim != 3 or frame.shape[2] != 3:
                raise ValueError("输入数组必须是三维RGB格式 (H, W, 3)")
            self._data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            raise TypeError("输入必须是PIL.Image或numpy.ndarray")

    @property
    def rgb_array(self) -> np.ndarray:
        """获取RGB格式的numpy数组"""
        return self._data.copy()

    @property
    def bgr_array(self) -> np.ndarray:
        """获取BGR格式的numpy数组"""
        return cv2.cvtColor(self._data, cv2.COLOR_RGB2BGR)

    def to_pil(self) -> Image.Image:
        """转换为PIL图像对象"""
        return Image.fromarray(self._data)

    def save(self, path: str, quality: int = 95) -> None:
        """保存图像到指定路径"""
        self.to_pil().save(path, quality=quality)

    def to_png_bytes(self) -> bytes:
        """生成PNG格式字节流"""
        success, buffer = cv2.imencode('.png', self.bgr_array)
        if not success:
            raise FrameEncodeError("PNG编码失败")
        return buffer.tobytes()