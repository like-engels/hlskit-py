class FfmpegCommandBuilder:

    @classmethod
    def build_simple_hls(
        cls,
        width: int,
        height: int,
        crf: int,
        preset: str,
        segment_filename: str,
        playlist_filename: str,
        hls_time: int = 10
    ) -> list[str]:

        command = [
            "ffmpeg",
            "-i", "pipe:0",
            "-vf", f"scale={width}:{height}",
            "-c:v", "libx264",
            "-crf", str(crf),
            "-preset", preset,
            "-hls_time", str(hls_time),
            "-hls_playlist_type", "vod",
            "-hls_segment_filename", segment_filename,
            playlist_filename
        ]
        
        return command
