# setup.py
from setuptools import setup, find_packages

setup(
    name="ffmpeg_installer",
    version="0.1.1",
    description="A Python package to install and use ffmpeg",
    author="Vinay Kumar K V",
    author_email="vinaykumar.kv@outlook.com",
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package needs
    ],
    entry_points={
        'console_scripts': [
            'install-ffmpeg=ffmpeg_installer.install_ffmpeg:install_ffmpeg',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

