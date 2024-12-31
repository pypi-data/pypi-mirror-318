from setuptools import setup, find_packages

setup(
    name="kamera",  # Package name
    version="0.2.2",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    description="A simple webcam streaming package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cobanov/kamera",  # Replace with your GitHub URL
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[
        "fastapi",
        "uvicorn",
        "opencv-python",
        "jinja2",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
