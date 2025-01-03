# hydra_youtube_api/cli.py
import argparse
import asyncio
import json
from . import get_data, filter_formats, get_lyrics

async def main():
    parser = argparse.ArgumentParser(description="Fast and simple API for YouTube and YouTube Music.")
    parser.add_argument("video_id", help="YouTube video ID")
    parser.add_argument("--bestaudio", action="store_true", help="Fetch the best audio format")
    parser.add_argument("--bestvideo", action="store_true", help="Fetch the best video format")
    parser.add_argument("--lowestaudio", action="store_true", help="Fetch the lowest quality audio format")
    parser.add_argument("--lowestvideo", action="store_true", help="Fetch the lowest quality video format")
    parser.add_argument("--videoandaudio", action="store_true", help="Fetch a format with both video and audio")
    parser.add_argument("--videoonly", action="store_true", help="Fetch a video-only format")
    parser.add_argument("--audioonly", action="store_true", help="Fetch an audio-only format")
    parser.add_argument("--lyrics", action="store_true", help="Fetch lyrics for the video")
    args = parser.parse_args()

    video_id = args.video_id

    # Fetch data from YouTube
    data = await get_data(video_id, client_name="ios")

    if args.bestaudio:
        # Fetch the best audio format
        best_audio = filter_formats(data, filter_type="bestaudio")
        if best_audio:
            print("Best Audio Format:")
            print(json.dumps(best_audio, indent=4))
        else:
            print("No audio format found.")

    elif args.bestvideo:
        # Fetch the best video format
        best_video = filter_formats(data, filter_type="bestvideo")
        if best_video:
            print("Best Video Format:")
            print(json.dumps(best_video, indent=4))
        else:
            print("No video format found.")

    elif args.lowestaudio:
        # Fetch the lowest quality audio format
        lowest_audio = filter_formats(data, filter_type="lowestaudio")
        if lowest_audio:
            print("Lowest Audio Format:")
            print(json.dumps(lowest_audio, indent=4))
        else:
            print("No audio format found.")

    elif args.lowestvideo:
        # Fetch the lowest quality video format
        lowest_video = filter_formats(data, filter_type="lowestvideo")
        if lowest_video:
            print("Lowest Video Format:")
            print(json.dumps(lowest_video, indent=4))
        else:
            print("No video format found.")

    elif args.videoandaudio:
        # Fetch a format with both video and audio
        video_and_audio = filter_formats(data, filter_type="videoandaudio")
        if video_and_audio:
            print("Video and Audio Format:")
            print(json.dumps(video_and_audio, indent=4))
        else:
            print("No format with both video and audio found.")

    elif args.videoonly:
        # Fetch a video-only format
        video_only = filter_formats(data, filter_type="videoonly")
        if video_only:
            print("Video-Only Format:")
            print(json.dumps(video_only, indent=4))
        else:
            print("No video-only format found.")

    elif args.audioonly:
        # Fetch an audio-only format
        audio_only = filter_formats(data, filter_type="audioonly")
        if audio_only:
            print("Audio-Only Format:")
            print(json.dumps(audio_only, indent=4))
        else:
            print("No audio-only format found.")

    elif args.lyrics:
        # Fetch and display lyrics
        lyrics = await get_lyrics(video_id)
        if lyrics:
            print("Lyrics:")
            print(lyrics)
        else:
            print("No lyrics found.")

    else:
        # If no specific flags are provided, print the raw response of get_data
        print(json.dumps(data, indent=4))  # Pretty-print the JSON response

def cli():
    asyncio.run(main())

if __name__ == "__main__":
    cli()