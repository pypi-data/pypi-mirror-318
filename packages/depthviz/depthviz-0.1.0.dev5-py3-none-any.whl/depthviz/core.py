"""
Module to create a video that reports the depth in meters from an array input.
"""

import os.path
from typing import Tuple
from moviepy import TextClip, VideoClip, concatenate_videoclips

# from depthviz.csv_parser import CsvParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DepthReportVideoCreatorError(Exception):
    """Base class for exceptions in this module."""


class VideoNotRenderError(DepthReportVideoCreatorError):
    """Exception raised for video not rendered errors."""


class VideoFormatError(DepthReportVideoCreatorError):
    """Exception raised for invalid video format errors."""


class DepthReportVideoCreator:
    """
    Class to create a video that reports the depth in meters from an array input.
    """

    def __init__(
        self,
        sample_rate: float = 0.250,
        font: str = os.path.abspath(
            os.path.join(BASE_DIR, "assets/fonts/Open_Sans/static/OpenSans-Bold.ttf")
        ),
        fontsize: int = 100,
        interline: int = -20,
        color: str = "white",
        bg_color: str = "black",
        stroke_color: str = "black",
        stroke_width: int = 2,
        align: str = "center",
        size: Tuple[int, int] = (640, 360),
    ):
        self.sample_rate = sample_rate
        self.font = font
        self.fontsize = fontsize
        self.interline = interline
        self.color = color
        self.bg_color = bg_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.align = align
        self.size = size
        self.final_video = None

    def render_depth_report_video(self, depth_data: list[float]) -> None:
        """
        Creates a video that reports the depth in meters from an array input.

        Args:
            depth_data: An array of depth values in meters.

        Returns:
            The processed video.
        """

        # Create a text clip for each depth value
        clips = []
        for _, depth in enumerate(depth_data):
            rounded_depth = round(depth)
            if rounded_depth == 0:
                text = "0m"
            else:
                text = f"-{rounded_depth}m"
            clip = TextClip(
                text=text,
                font=self.font,
                font_size=self.fontsize,
                interline=self.interline,
                color=self.color,
                bg_color=self.bg_color,
                stroke_color=self.stroke_color,
                stroke_width=self.stroke_width,
                text_align=self.align,
                size=self.size,
                duration=self.sample_rate,
            )
            clips.append(clip)

        # Concatenate all the clips into a single video
        self.final_video = concatenate_videoclips(clips)

    def save(self, path: str, fps: int = 25) -> None:
        """
        Saves the video to a file.

        Args:
            path: The path to save the video (expected file format: .mp4).
            fps: The frames per second of the video.
        """
        parent_dir = os.path.dirname(path)
        if parent_dir == "":
            parent_dir = "./"
        if os.path.exists(parent_dir):
            if os.path.isdir(path):
                raise NameError(
                    f"{path} is a directory, please add a file name to the path. \
                        (e.g., path/to/mydepth_video.mp4)"
                )
            if self.final_video is not None:
                if not path.endswith(".mp4"):
                    raise VideoFormatError(
                        "Invalid file format: The file format must be .mp4"
                    )
                self.final_video.write_videofile(path, fps=fps)
            else:
                raise VideoNotRenderError(
                    "Cannot save video because it has not been rendered yet."
                )
        else:
            raise FileNotFoundError(f"Parent directory does not exist: {parent_dir}")

    def get_video(self) -> VideoClip:
        """
        Returns the processed video.

        Returns:
            The processed video.
        """
        return self.final_video
