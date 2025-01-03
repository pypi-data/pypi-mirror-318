# hydra_youtube_api/cli.py
import argparse
import asyncio
import json
import sys
from . import get_data, filter_formats, get_lyrics

# Define supported filter types
SUPPORTED_FILTERS = {
    "bestaudio": "Fetch the best audio format",
    "bestvideo": "Fetch the best video format",
    "lowestaudio": "Fetch the lowest quality audio format",
    "lowestvideo": "Fetch the lowest quality video format",
    "videoandaudio": "Fetch a format with both video and audio",
    "videoonly": "Fetch a video-only format",
    "audioonly": "Fetch an audio-only format",
    "lyrics": "Fetch lyrics for the video",
}

async def fetch_and_print_formats(video_id, filter_type):
    """Fetch and print formats based on the filter type."""
    try:
        # Fetch data from YouTube
        data = await get_data(video_id, client_name="ios")
        
        # Apply the filter
        result = filter_formats(data, filter_type=filter_type)
        
        if result:
            print(f"{filter_type.capitalize()} Format:")
            print(json.dumps(result, indent=4))
        else:
            print(f"No {filter_type} format found.")
    except Exception as e:
        print(f"Error fetching {filter_type}: {e}", file=sys.stderr)

async def fetch_lyrics(video_id):
    """Fetch and print lyrics for the video."""
    try:
        lyrics = await get_lyrics(video_id)
        if lyrics:
            print("Lyrics:")
            print(lyrics)
        else:
            print("No lyrics found.")
    except Exception as e:
        print(f"Error fetching lyrics: {e}", file=sys.stderr)

async def print_raw_data(video_id):
    """Print the raw response from get_data."""
    try:
        data = await get_data(video_id, client_name="ios")
        print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"Error fetching raw data: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(
        description="Fast and simple API for YouTube and YouTube Music.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("video_id", help="YouTube video ID")

    # Add filter arguments dynamically
    for filter_type, help_text in SUPPORTED_FILTERS.items():
        parser.add_argument(
            f"--{filter_type}",
            action="store_true",
            help=help_text,
        )

    args = parser.parse_args()

    # Determine which action to take based on the provided arguments
    for filter_type in SUPPORTED_FILTERS:
        if getattr(args, filter_type):
            asyncio.run(fetch_and_print_formats(args.video_id, filter_type))
            break
    else:
        if args.lyrics:
            asyncio.run(fetch_lyrics(args.video_id))
        else:
            # Default behavior: print raw data
            asyncio.run(print_raw_data(args.video_id))

if __name__ == "__main__":
    main()