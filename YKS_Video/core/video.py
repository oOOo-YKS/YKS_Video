import cv2
from typing import List, Generator
from pathlib import Path
from ..exceptions import VideoOpenError, FrameReadError
from .frame import Frame

class Video:
    def __init__(self, path: str):
        self._path = Path(path).resolve()
        self._cap = cv2.VideoCapture(str(self._path))
        
        if not self._cap.isOpened():
            raise VideoOpenError(f"无法打开视频文件: {self._path}")

        self._fps = self._cap.get(cv2.CAP_PROP_FPS)
        self._validate_fps()
        
        self.width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.total_frames = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.total_frames / self.fps if self.fps > 0 else 0
        
        self._fourcc = self._get_fourcc()

    def _validate_fps(self):
        """验证帧率有效性"""
        if self._fps <= 0:
            raise VideoOpenError("无效的视频帧率，可能文件已损坏")

    def _get_fourcc(self) -> str:
        """获取四字符编码"""
        code = int(self._cap.get(cv2.CAP_PROP_FOURCC))
        return "".join([chr((code >> 8*i) & 0xFF) for i in range(4)])

    @property
    def fps(self) -> float:
        """获取视频帧率"""
        return self._fps

    @property
    def fourcc(self) -> str:
        """获取视频编码格式"""
        return self._fourcc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

    def release(self):
        """显式释放视频资源"""
        if self._cap.isOpened():
            self._cap.release()

    def get_frame(self, frame_number: int) -> Frame:
        """获取指定帧"""
        if frame_number < 0 or frame_number >= self.total_frames:
            raise ValueError(f"帧号需在[0, {self.total_frames-1}]之间")

        self._cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self._cap.read()
        
        if not ret or frame is None:
            raise FrameReadError(f"读取第{frame_number}帧失败")
            
        return Frame(frame)

    def iter_frames(self) -> Generator[Frame, None, None]:
        """迭代生成所有帧"""
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        while True:
            ret, frame = self._cap.read()
            if not ret:
                break
            yield Frame(frame)

    def get_frames_in_sec(self, sec: int):
        """获取指定秒数的帧"""
        start_index = int(sec * self.fps)
        end_index = int((sec + 1) * self.fps)
        start_index = max(0, start_index)
        end_index = min(end_index, self.total_frames)
        if start_index >= end_index:
            raise ValueError(f"无效的时间范围: {sec}秒")
        indexs = range(start_index, end_index)
        frames = [self.get_frame(i) for i in range(start_index, end_index)]
        return indexs, frames
