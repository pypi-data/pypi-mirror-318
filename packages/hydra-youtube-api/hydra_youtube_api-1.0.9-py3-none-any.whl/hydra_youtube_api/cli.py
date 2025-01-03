# hydra_youtube_api/cli.py
import argparse
import asyncio
from . import get_data, filter_formats, get_lyrics

async def main():
    parser = argparse.ArgumentParser(description="Fast and simple API for YouTube and YouTube Music.")
    parser.add_argument("video_id", help="YouTube video ID")
    parser.add_argument("--formats", action="store_true", help="List available formats")
    parser.add_argument("--lyrics", action="store_true", help="Fetch lyrics for the video")
    args = parser.parse_args()

    video_id = args.video_id

    if args.formats:
        # Fetch and list available formats
        data = await get_data(video_id, client_name="ios")
        formats = filter_formats(data, filter_type="all")
        for fmt in formats:
            print(f"Format: {fmt.get('mimeType')}, Resolution: {fmt.get('width')}x{fmt.get('height')}, Bitrate: {fmt.get('bitrate')}")

    if args.lyrics:
        # Fetch and display lyrics
        lyrics = await get_lyrics(video_id)
        if lyrics:
            print("Lyrics:")
            print(lyrics)
        else:
            print("No lyrics found.")

def cli():
    print("CLI function is being called!")  # Debug statement
    asyncio.run(main())

if __name__ == "__main__":
    print("Running cli.py directly!")  # Debug statement
    cli()