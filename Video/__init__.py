"""
视频处理核心库

提供以下主要功能：
- Video 类：视频元数据解析与帧操作
- Frame 类：跨格式帧数据转换与保存
- 异常体系：明确的错误处理机制

示例用法：
>>> from video_lib import Video
>>> with Video("input.mp4") as video:
...     frame = video.get_frame(0)
...     frame.save("first_frame.jpg")
"""

__version__ = "1.0.2"  # 遵循语义化版本规范 (SemVer)
__all__ = [
    'Video',
    'Frame',
    'VideoError',
    'VideoOpenError',
    'FrameReadError',
    'FrameEncodeError'
]

# 显式导入公共API
from .core.video import Video
from .core.frame import Frame

# 导入异常体系
from .exceptions import (
    VideoError,
    VideoOpenError,
    FrameReadError,
    FrameEncodeError
)

# 初始化校验
try:
    import cv2
    from PIL import Image
except ImportError as e:
    raise RuntimeError("依赖库缺失，请确认已安装 opencv-python 和 Pillow") from e