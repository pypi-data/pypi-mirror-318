from typing_extensions import TypedDict
from typing import Literal

class VideoInfo(TypedDict):
    """Type definitions for video information dictionary."""
    duration: float
    width: int
    height: int
    fps: float
    codec: str
    bitrate: str

ColorType = Literal['white', 'black', 'gray', 'custom']
