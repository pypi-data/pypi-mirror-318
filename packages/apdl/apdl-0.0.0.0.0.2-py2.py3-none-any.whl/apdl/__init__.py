"""
apdl - A Python package for downloading YouTube videos in MP3 and MP4 formats.

This module provides functionality for downloading YouTube videos in various
quality options (MP3 and MP4) through both a command-line interface (CLI) and
Python script. It supports different quality options for audio and video,
and allows easy integration into other Python projects.
"""


__version__ = "0.0.0.0.0.2"
from .cli import (
    fetch_video_info,
    mp3_mode,
    mp4_mode,
    thumbnail_mode
)

__all__ = [
    'fetch_video_info',
    'thumbnail_mode',
    'mp3_mode',
    'mp4_mode',
]
