import asyncio

from hlskit_py import HlsVideoProcessingSettings, HlsVideoProcessor


async def process_videos():
    input_dir = "example/sample.mp4"

    with open(input_dir, "rb") as video_binary:
        input_bytes = video_binary.read()

    tasks = [
        HlsVideoProcessor.process_video(
            input_bytes=input_bytes,
            output_profiles=[
                HlsVideoProcessingSettings(
                    resolution=(1920, 1080),
                    constant_rate_factor=28,
                ),
                HlsVideoProcessingSettings(
                    resolution=(1280, 720),
                    constant_rate_factor=28,
                ),
                HlsVideoProcessingSettings(
                    resolution=(854, 480),
                    constant_rate_factor=28,
                ),
            ],
        )
        for _ in range(0, 1)
    ]

    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    results = asyncio.run(process_videos())
