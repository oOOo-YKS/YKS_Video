# YKS_Video

一个简单易用的视频处理库，提供视频帧提取和处理功能。

## 功能特点

- 视频元数据解析（帧率、分辨率、时长等）
- 单帧提取和保存
- 帧遍历器支持
- 跨格式帧数据转换（OpenCV ↔ PIL ↔ NumPy）
- 异常处理机制

## 安装

```bash
pip install YKS_Video
```

## 依赖要求

- Python >= 3.8
- opencv-python >= 4.5
- numpy >= 1.19
- Pillow >= 8.3

## 使用示例

### 基本用法

```python
from YKS_Video import Video

# 使用上下文管理器自动释放资源
with Video("input.mp4") as video:
    # 获取视频信息
    print(f"分辨率: {video.width}x{video.height}")
    print(f"帧率: {video.fps}")
    print(f"总帧数: {video.total_frames}")
    print(f"时长: {video.duration:.2f}秒")
    
    # 提取第一帧并保存
    frame = video.get_frame(0)
    frame.save("first_frame.jpg")
    
    # 转换为PIL图像
    pil_image = frame.to_pil()
    
    # 获取RGB格式的numpy数组
    rgb_array = frame.rgb_array
```

### 遍历所有帧

```python
with Video("input.mp4") as video:
    for i, frame in enumerate(video.iter_frames()):
        # 处理每一帧
        frame.save(f"frame_{i:04d}.jpg")
```

## 异常处理

```python
from YKS_Video import Video, VideoOpenError, FrameReadError

try:
    with Video("non_existent.mp4") as video:
        frame = video.get_frame(0)
except VideoOpenError as e:
    print(f"视频打开失败: {e}")
except FrameReadError as e:
    print(f"帧读取失败: {e}")
```

## 许可证

MIT License
