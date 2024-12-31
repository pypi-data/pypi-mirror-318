from setuptools import setup, find_packages

setup(
    name="kamera",
    version="0.2.1",
    description="Stream your webcam with adjustable settings using FastAPI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    url="https://github.com/cobanov/kamera",
    packages=find_packages(),
    include_package_data=True,  # Includes templates and static files
    install_requires=[
        "fastapi",
        "uvicorn",
        "jinja2",
        "opencv-python",
    ],
    entry_points={
        "console_scripts": [
            "kamera=kamera.app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
