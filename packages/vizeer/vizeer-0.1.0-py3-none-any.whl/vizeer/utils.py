from pymediainfo import MediaInfo
from typing import Tuple
import re
from .types import VideoInfo, ColorType

def get_video_info(video_path: str) -> VideoInfo:
    """Extract media information from video file.

    Args:
        video_path: Path to the video file.

    Returns:
        Dictionary containing video metadata.

    Raises:
        ValueError: If video track cannot be found in the file.
    """
    media_info = MediaInfo.parse(video_path)
    video_track = next((track for track in media_info.tracks
                       if track.track_type == "Video"), None)

    if not video_track:
        raise ValueError("No video track found in file")

    return {
        'duration': float(video_track.duration) / 1000 if video_track.duration else 0,
        'width': video_track.width,
        'height': video_track.height,
        'fps': float(video_track.frame_rate),
        'codec': video_track.codec,
        'bitrate': f"{int(video_track.bit_rate/1000) if video_track.bit_rate else 0}kbps"
    }

def format_timestamp(seconds: float) -> str:
    """Format seconds into HH:MM:SS.

    Args:
        seconds: Number of seconds to format.

    Returns:
        Formatted timestamp string.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def parse_color(color: str) -> Tuple[int, int, int]:
    """Parse color string into RGB tuple.

    Args:
        color: Color string in format 'rgb(r,g,b)' or predefined color name.

    Returns:
        Tuple of (r, g, b) values.

    Raises:
        ValueError: If color string is invalid.
    """
    if color == 'white':
        return (255, 255, 255)
    elif color == 'black':
        return (0, 0, 0)
    elif color == 'gray':
        return (128, 128, 128)

    rgb_match = re.match(r'rgb\((\d+),(\d+),(\d+)\)', color)
    if rgb_match:
        r, g, b = map(int, rgb_match.groups())
        if all(0 <= x <= 255 for x in (r, g, b)):
            return (r, g, b)

    raise ValueError(
        "Color must be 'white', 'black', 'gray' or in format 'rgb(r,g,b)'"
    )
