"""Youtube Search"""
import argparse
import os
import sys

from dotenv import load_dotenv

import search_videos
from search_videos import search_videos
from video_details import video_details, print_video_details

parser = argparse.ArgumentParser(description="Youtube Search")
parser.add_argument("-c", "--channel", action="store", help="Channel ID (required)")
parser.add_argument(
    "-r", "--results", action="store", help="Number of results", default=1
)

args = parser.parse_args()

if not args.channel:
    print("Please specify a channel ID")
    sys.exit(1)

load_dotenv()
api_key = os.getenv("YOUTUBE_DATA_API_KEY")
search_results = search_videos(args.channel, api_key, args.results)
if search_results.get("error"):
    print(search_results["error"]["message"])
    sys.exit(1)

video_ids = [video["id"]["videoId"] for video in search_results.get("items", [])]
videos = video_details(video_ids, api_key)
if videos.get("error"):
    print(search_results["error"]["message"])
    sys.exit(1)
print_video_details(videos)
