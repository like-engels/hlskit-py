from typing import Literal

from pydantic import BaseModel


class HlsVideoProcessingSettings(BaseModel):
    resolution: tuple[int, int]
    constant_rate_factor: int
    preset: Literal[
        "veryslow",
        "slower",
        "slow",
        "medium",
        "fast",
        "faster",
        "veryfast",
        "superfast",
        "ultrafast",
    ] = "medium"
