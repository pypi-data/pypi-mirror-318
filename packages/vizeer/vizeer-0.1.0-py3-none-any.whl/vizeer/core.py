import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import math
from typing import Optional, Tuple

import click
from vizeer.scene import detect_scenes, select_representative_frames
from vizeer.utils import get_video_info, format_timestamp, parse_color
from vizeer.types import VideoInfo, ColorType

class Generator:
    """Generate contact sheets from video files with scene detection.

    This class handles the creation of contact sheets from videos, including
    scene detection, frame selection, and layout generation.

    Attributes:
        video_path: Path to the source video file.
        info: Dictionary containing video metadata.
    """

    def __init__(self, video_path: str):
        """Initialize the contact sheet generator.

        Args:
            video_path: Path to the video file to process.

        Raises:
            ValueError: If the video file cannot be accessed.
        """
        self.video_path = video_path
        self.info = get_video_info(video_path)

    def create_sheet(self,
                    num_screenshots: int = 6,
                    output_path: str = "contact_sheet.jpg",
                    min_scene_length: int = 30,
                    bg_color: str = 'white') -> str:
        """Create a contact sheet from video screenshots.

        Args:
            num_screenshots: Number of screenshots to include in the sheet.
            output_path: Path where the output image will be saved.
            min_scene_length: Minimum frames between detected scenes.
            bg_color: Background color for the contact sheet.
                     Can be 'white', 'black', 'gray' or 'rgb(r,g,b)'.

        Returns:
            Path to the generated contact sheet image.

        Raises:
            ValueError: If the video cannot be processed or invalid color.
        """
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise ValueError("Could not open video file")

        bg_rgb = parse_color(bg_color)

        # Detect scenes and select frames
        scene_changes = detect_scenes(self.video_path, min_scene_length)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        selected_frames = select_representative_frames(
            scene_changes, num_screenshots, total_frames)

        # Calculate dimensions
        cols = min(3, num_screenshots)
        rows = math.ceil(num_screenshots / cols)
        frame_width = int(self.info['width'])
        frame_height = int(self.info['height'])
        thumb_width = 640
        thumb_height = int(thumb_width * frame_height / frame_width)

        # Create sheet
        sheet_width = thumb_width * cols
        sheet_height = thumb_height * rows + 150
        contact_sheet = Image.new('RGB', (sheet_width, sheet_height), bg_rgb)
        draw = ImageDraw.Draw(contact_sheet)

        # Add header with contrasting color
        header_color = 'black' if sum(bg_rgb) > 382 else 'white'
        try:
            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        except Exception as e:
            font = ImageFont.load_default()

        header_text = self._create_header_text(len(scene_changes))
        draw.text((20, 20), header_text, font=font, fill=header_color)

        # Add screenshots
        with click.progressbar(
            selected_frames,
            label='Generating contact sheet'
        ) as frames:
            for idx, frame_pos in enumerate(frames):
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)
                ret, frame = cap.read()
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pil_image = Image.fromarray(frame_rgb)
                    pil_image = pil_image.resize(
                        (thumb_width, thumb_height),
                        Image.Resampling.LANCZOS
                    )

                    row = idx // cols
                    col = idx % cols
                    x = col * thumb_width
                    y = row * thumb_height + 150

                    contact_sheet.paste(pil_image, (x, y))

                    timestamp = format_timestamp(frame_pos / self.info['fps'])
                    frame_info = f"{timestamp} (Frame: {frame_pos})"
                    draw.text(
                        (x + 10, y + 10),
                        frame_info,
                        font=font,
                        fill='white',
                        stroke_width=2,
                        stroke_fill='black'
                    )

        # Save and cleanup
        contact_sheet.save(output_path, quality=95)
        cap.release()
        return output_path

    def _create_header_text(self, num_scenes: int) -> str:
        """Create the header text with video information.

        Args:
            num_scenes: Number of detected scenes in the video.

        Returns:
            Formatted header text string.
        """
        return (
            f"Filename: {os.path.basename(self.video_path)}\n"
            f"Resolution: {self.info['width']}x{self.info['height']} | "
            f"Duration: {int(self.info['duration'])}s | "
            f"FPS: {self.info['fps']} | "
            f"Codec: {self.info['codec']} | "
            f"Bitrate: {self.info['bitrate']} | "
            f"Scenes: {num_scenes}"
        )
