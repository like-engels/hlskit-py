from dataclasses import dataclass, field


@dataclass
class HlsVideoSegment:
    segment_name: str
    segment_data: bytes


@dataclass
class HlsVideoResolution:
    resolution: tuple[int, int]
    playlist_name: str
    playlist_data: bytes = field(init=False)
    segments: list[HlsVideoSegment]


@dataclass
class HlsVideo:
    master_m3u8_data: bytes
    resolutions: list[HlsVideoResolution]
