import asyncio
import os
import tempfile

from ..models import (
    HlsVideo,
    HlsVideoProcessingSettings,
    HlsVideoResolution,
    HlsVideoSegment,
)
from ..tools import FfmpegCommandBuilder, M3u8Tools


class HlsVideoProcessor:
    @classmethod
    async def process_video(
        cls,
        input_bytes: bytes,
        output_profiles: list[HlsVideoProcessingSettings],
    ) -> HlsVideo:
        """
        Process the video concurrently for multiple resolutions and generate HLS files.
        Returns a dictionary containing all playlists and segments in bytes.
        """

        temp_dir = tempfile.TemporaryDirectory()
        output_dir = temp_dir.name

        tasks = [
            cls.process_video_profile(
                input_bytes,
                profile.resolution,
                profile.constant_rate_factor,
                profile.preset,
                output_dir,
                idx,
            )
            for idx, profile in enumerate(output_profiles)
        ]

        resolution_results = await asyncio.gather(*tasks)

        playlist_filenames = [
            f"{output_dir}/{resolution.playlist_name}"
            for _, resolution in enumerate(resolution_results)
        ]

        overall_resolutions = [
            result.resolution for _, result in enumerate(resolution_results)
        ]

        master_playlist_bytes = await M3u8Tools.generate_master_playlist(
            output_dir=output_dir,
            resolutions=overall_resolutions,
            playlist_filenames=playlist_filenames,
        )

        hls_video = HlsVideo(
            master_m3u8_data=master_playlist_bytes, resolutions=resolution_results
        )

        temp_dir.cleanup()

        return hls_video

    @classmethod
    async def process_video_profile(
        cls,
        input_bytes: bytes,
        resolution: tuple[int, int],
        crf: int,
        preset: str,
        output_dir: str,
        stream_index: int,
    ) -> HlsVideoResolution:
        """
        Process a single resolution of the video and generate HLS segments.
        Returns an HlsVideoResolution object.
        """

        width, height = resolution
        segment_filename = f"{output_dir}/data_{stream_index}_%03d.ts"
        playlist_filename = f"{output_dir}/playlist_{stream_index}.m3u8"

        # Create temporary file for input video bytes
        temp_input_file = tempfile.NamedTemporaryFile(delete=False, suffix=".tmp")
        try:
            # Write input bytes to temporary file
            temp_input_file.write(input_bytes)
            temp_input_file.flush()

            command = FfmpegCommandBuilder.build_simple_hls(
                input_file_path=temp_input_file.name,
                width=width,
                height=height,
                crf=crf,
                preset=preset,
                segment_filename=segment_filename,
                playlist_filename=playlist_filename,
            )

            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            _, stderr = await process.communicate()

            if process.returncode != 0:
                raise RuntimeError(
                    f"[HlsKit] FFmpeg error for resolution {width}x{height}: {stderr.decode()}"
                )
        finally:
            # Clean up temporary input file
            temp_input_file.close()
            if os.path.exists(temp_input_file.name):
                os.unlink(temp_input_file.name)

        hls_resolution = HlsVideoResolution(
            resolution=resolution,
            playlist_name=f"playlist_{stream_index}.m3u8",
            segments=[],
        )

        with open(playlist_filename, "rb") as playlist_file:
            hls_resolution.playlist_data = playlist_file.read()

        segment_index = 0

        while True:
            segment_path = segment_filename.replace("%03d", f"{segment_index:03d}")
            if not os.path.exists(segment_path):
                break
            with open(segment_path, "rb") as segment_file:
                segment_name = f"data_{stream_index}_%03d.ts".replace(
                    "%03d", f"{segment_index:03d}"
                )
                hls_resolution.segments.append(
                    HlsVideoSegment(
                        segment_name=segment_name,
                        segment_data=segment_file.read(),
                    )
                )
            segment_index += 1

        return hls_resolution
