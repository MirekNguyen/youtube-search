"""Youtube Search"""
import os
import sys

import argparse
import requests
from dotenv import load_dotenv

parser = argparse.ArgumentParser(description="Youtube Search")
parser.add_argument("-c", "--channel", action="store", help="Channel ID (required)")

args = parser.parse_args()

if not args.channel:
    print("Please specify a channel ID")
    sys.exit(1)

load_dotenv()
api_key = os.getenv("YOUTUBE_DATA_API_KEY")
channel_id = args.channel
BASE_VIDEO_URL = "https://www.googleapis.com/youtube/v3/search?"

params = {
    "part": "snippet",
    "channelId": channel_id,
    "maxResults": 1,
    "order": "date",
    "type": "video",
    "key": api_key,
}

response = requests.get(BASE_VIDEO_URL, params=params, timeout=5)
if response.status_code != 200:
    print("Error: ", response.status_code)
    sys.exit(1)

search_results = response.json()
video_ids = [video["id"]["videoId"] for video in search_results.get("items", [])]
print(video_ids)
