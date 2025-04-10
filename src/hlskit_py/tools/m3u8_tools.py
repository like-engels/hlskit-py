import os


class M3u8Tools:
    @classmethod
    async def generate_master_playlist(
        cls,
        output_dir: str,
        resolutions: list[tuple[int, int]],
        playlist_filenames: list[str],
    ) -> bytes:
        """
        Generate the master.m3u8 file for adaptive bitrate streaming and return its bytes.
        """

        master_playlist_path = os.path.join(output_dir, "master.m3u8")

        with open(master_playlist_path, "w") as master_playlist:
            master_playlist.write("#EXTM3U\n")

            for idx, (width, height) in enumerate(resolutions):
                playlist_path = os.path.basename(playlist_filenames[idx])
                master_playlist.write(
                    f"#EXT-X-STREAM-INF:BANDWIDTH={int((idx + 1)) * 1500000},RESOLUTION={width}x{height}\n"
                )
                master_playlist.write(f"{playlist_path}\n")
                print(f"[HslKit] Master playlist created for {width}x{height}")

        with open(master_playlist_path, "rb") as master_file:
            return master_file.read()
