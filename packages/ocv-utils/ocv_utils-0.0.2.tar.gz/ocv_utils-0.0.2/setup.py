from setuptools import setup, find_packages

setup(
    name="ocv_utils",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.0",
    ],
    author="Alpe6825",
    description="Simplifies OpenCV functionalities for image and video i/o and debug-windows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alpe6825/ocv_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)