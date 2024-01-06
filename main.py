"""Youtube Search"""
import argparse
import os
import sys

from dotenv import load_dotenv

import search_videos
from feed_generator import generate_fg, generate_video_rss
from search_videos import search_videos, search_playlist_videos
from video_details import video_details, video_info
from playlist import get_playlist_id

def handle_error(error):
    """Handle errors"""
    if error:
        print(error)
        sys.exit(1)

parser = argparse.ArgumentParser(description="Youtube Search")
parser.add_argument("-c", "--channel", action="store", help="Channel ID (required)")
parser.add_argument(
    "-r", "--results", action="store", help="Number of results", default=1
)
parser.add_argument("-o", "--output", action="store", help="Generate RSS feed")
parser.add_argument("-t", "--timezone", action="store", help="Timezone")
parser.add_argument("-p", "--playlist", action="store", help="Playlist ID")
parser.add_argument("--get-playlist", action="store", help="Get playlist ID from channel ID")

args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("YOUTUBE_DATA_API_KEY", os.getenv("YOUTUBE_DATA_API_KEY"))

if args.get_playlist:
    response = get_playlist_id(args.get_playlist, api_key)
    if response.status_code != 200:
        print("Channel ID is valid")
        sys.exit(1)
    data = response.json()
    uploads_playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print(f'The playlist ID for the channel uploads is: {uploads_playlist_id}')
    sys.exit(0)

if not args.channel and not args.playlist:
    print("Please specify a channel or playlist ID")
    sys.exit(1)

if args.playlist:
    search_results = search_playlist_videos(args.playlist, api_key, args.results)
    handle_error(search_results.get("error"))
    video_ids = [video["contentDetails"]["videoId"] for video in search_results.get("items", [])]
else:
    search_results = search_videos(args.channel, api_key, args.results)
    handle_error(search_results.get("error"))
    video_ids = [video["id"]["videoId"] for video in search_results.get("items", [])]

videos = video_details(video_ids, api_key)
handle_error(videos.get("error"))

videos = video_info(videos)

if args.output:
    fg = generate_fg(
        feed_id="https://www.youtube.com/channel/" + args.channel,
        title="Youtube Search",
        subtitle="Youtube Search",
        link="https://www.youtube.com/channel/" + args.channel,
        language="en",
    )
    if args.timezone:
        generate_video_rss(videos, fg, args.output, args.timezone)
    else:
        generate_video_rss(videos, fg, args.output)
else:
    print(videos)
