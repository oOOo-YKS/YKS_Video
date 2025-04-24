from YKS_Video import Video
import sys

def test_video_info(video_path):
    """测试视频基本信息读取"""
    try:
        with Video(video_path) as video:
            print(f"视频信息:")
            print(f"- 分辨率: {video.width}x{video.height}")
            print(f"- 帧率: {video.fps}")
            print(f"- 总帧数: {video.total_frames}")
            print(f"- 时长: {video.duration:.2f}秒")
            print(f"- 编码格式: {video.fourcc}")
            
            # 尝试读取第一帧
            frame = video.get_frame(0)
            frame.save("first_frame.jpg")
            print("\n成功提取第一帧并保存为 first_frame.jpg")
            
    except Exception as e:
        print(f"错误: {e}")
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python test_video.py <视频文件路径>")
        sys.exit(1)
        
    video_path = sys.argv[1]
    success = test_video_info(video_path)
    sys.exit(0 if success else 1)
