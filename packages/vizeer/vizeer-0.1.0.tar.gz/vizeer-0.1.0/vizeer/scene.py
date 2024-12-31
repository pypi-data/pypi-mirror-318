import cv2
import numpy as np
from typing import List
import click
from moviepy.video.io.VideoFileClip import VideoFileClip

def detect_scenes(video_path: str, min_scene_length: float = 2.0) -> List[float]:
    """
    Detect scene changes in video using frame differences with OpenCV.

    Args:
        video_path: Path to the video file to analyze.
        min_scene_length: Minimum duration (in seconds) between detected scenes.

    Returns:
        List of timestamps (in seconds) where scene changes were detected.

    Raises:
        ValueError: If the video file cannot be opened.
    """
    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video file")

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    min_frame_gap = int(min_scene_length * fps)  # Minimum frames between scenes

    # Initialize variables
    prev_frame = None
    scene_changes = []
    frame_diff_threshold = 30.0  # Adjust threshold for scene detection

    # Analyze frames for scene changes
    with click.progressbar(length=total_frames, label='Analyzing scenes') as bar:
        for frame_num in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Compare with previous frame
            if prev_frame is not None:
                frame_diff = np.mean(np.abs(gray_frame - prev_frame))

                # Detect scene change
                if frame_diff > frame_diff_threshold:
                    # Ensure minimum gap between scenes
                    if not scene_changes or (frame_num - scene_changes[-1]) >= min_frame_gap:
                        scene_changes.append(frame_num)

            prev_frame = gray_frame
            bar.update(1)

    # Convert frame numbers to timestamps
    scene_timestamps = [frame_num / fps for frame_num in scene_changes]

    # Release video capture
    cap.release()

    return scene_timestamps

def select_representative_frames(
    scene_timestamps: List[float],
    num_screenshots: int,
    video_duration: float
) -> List[float]:
    """
    Select representative timestamps from detected scenes.

    Args:
        scene_timestamps: List of timestamps (in seconds) where scenes change.
        num_screenshots: Number of screenshots to select.
        video_duration: Total duration of the video (in seconds).

    Returns:
        List of timestamps selected for screenshots.
    """
    if not scene_timestamps:
        interval = video_duration / (num_screenshots + 1)
        return [interval * (i + 1) for i in range(num_screenshots)]

    if len(scene_timestamps) < num_screenshots:
        return scene_timestamps + [
            video_duration * (i + 1) / (num_screenshots + 1)
            for i in range(num_screenshots - len(scene_timestamps))
        ]

    indices = np.linspace(0, len(scene_timestamps) - 1, num_screenshots, dtype=int)
    return [scene_timestamps[i] for i in indices]

def extract_frame_at_time(video_path: str, timestamp: float) -> np.ndarray:
    """
    Extract a frame from the video at a specific timestamp.

    Args:
        video_path: Path to the video file.
        timestamp: Timestamp (in seconds) to extract the frame.

    Returns:
        The extracted frame as a NumPy array.
    """
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise ValueError(f"Could not extract frame at timestamp {timestamp}")
    return frame
