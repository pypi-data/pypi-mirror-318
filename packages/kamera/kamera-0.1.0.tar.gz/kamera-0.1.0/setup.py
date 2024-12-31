from setuptools import setup, find_packages

setup(
    name="kamera",
    version="0.1.0",
    description="Stream your webcam over the network",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    url="https://github.com/cobanov/kamera",
    packages=find_packages(),
    install_requires=[
        "flask",
        "opencv-python",
    ],
    entry_points={
        "console_scripts": [
            "kamera=kamera.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
