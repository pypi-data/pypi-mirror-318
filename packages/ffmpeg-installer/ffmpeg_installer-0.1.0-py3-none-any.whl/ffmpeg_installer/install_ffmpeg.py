# ffmpeg_installer/install_ffmpeg.py
import subprocess
import sys

def install_ffmpeg():
    try:
        # Check if ffmpeg is already installed
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("ffmpeg is already installed.")
    except subprocess.CalledProcessError:
        print("Installing ffmpeg...")
        # Install ffmpeg
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "ffmpeg"], check=True)
        print("ffmpeg installed successfully.")

if __name__ == "__main__":
    install_ffmpeg()
