from pathlib import Path
from setuptools import setup, find_packages

# 安全读取README.md
def get_long_description():
    try:
        return (Path(__file__).parent / "README.md").read_text(encoding="utf-8")
    except FileNotFoundError:
        return "自用视频处理库"

setup(
    name="YKS_Video",
    version="0.1.5",
    packages=find_packages(include=["YKS_Video*"]),
    install_requires=[
        "opencv-python>=4.5",
        "numpy>=1.19",
        "Pillow>=8.3"
    ],
    author="oOOo-YKS",
    description="自用视频处理库",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/oOOo-YKS/YKS_Video",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    keywords="video processing opencv",
    project_urls={
        "Documentation": "https://github.com/oOOo-YKS/YKS_Video/wiki",
        "Bug Tracker": "https://github.com/oOOo-YKS/YKS_Video/issues",
    }
)