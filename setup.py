from setuptools import setup, find_packages

setup(
    name="YKS_Video",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.11.0.86",
        "numpy>=2.1.2",
        "Pillow>=10.4.0"
    ],
    author="oOOo-YKS",
    description="自用视频处理库",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/oOOo-YKS/YKS_Video",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)