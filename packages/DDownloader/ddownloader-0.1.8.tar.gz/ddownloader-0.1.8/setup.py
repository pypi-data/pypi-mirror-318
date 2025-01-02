from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README.md
long_description = Path("README.md").read_text(encoding="utf-8")

setup(
    name="DDownloader",
    version="0.1.8",
    description="A downloader for DRM-protected content.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ThatNotEasy",
    author_email="apidotmy@proton.me",
    url="https://github.com/ThatNotEasy/DDownloader",
    license="MIT",
    packages=find_packages(include=["DDownloader", "DDownloader.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.26.0",
        "coloredlogs>=15.0",
        "loguru>=0.6.0",
    ],
    entry_points={
        "console_scripts": [
            "DDownloader=DDownloader.main:main",
        ],
    }
)