class VideoError(Exception):
    """视频处理基础异常"""
    
class VideoOpenError(VideoError):
    """视频打开失败异常"""
    
class FrameReadError(VideoError):
    """帧读取失败异常"""
    
class FrameEncodeError(VideoError):
    """帧编码失败异常"""