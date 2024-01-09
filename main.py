"""Youtube Search"""
import argparse
import os
import sys

from dotenv import load_dotenv

from youtube_search.feed_generator import generate_fg, generate_video_rss
from youtube_search.search_videos import search_videos, search_playlist_videos
from youtube_search.video_details import video_details, video_info
from youtube_search.playlist import get_playlist_id
from youtube_search.search_videos import search_videos
from youtube_search.settings import Settings

def handle_error(error):
    """Handle errors"""
    if error:
        print(error)
        sys.exit(1)

settings = Settings()
settings.parse_args()
settings.load_env()
print(settings.env["api_key"])

if not settings.env["api_key"]:
    print("Invalid or non-existent Youtube API key")
    sys.exit(1)

if settings.args.get_playlist:
    response = get_playlist_id(settings.args.get_playlist, settings.env["api_key"])
    if response.status_code != 200:
        print(response.json().message)
        sys.exit(1)
    data = response.json()
    uploads_playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print(f'The playlist ID for the channel uploads is: {uploads_playlist_id}')
    sys.exit(0)

if not settings.args.channel and not settings.args.playlist:
    print("Please specify a channel or playlist ID")
    sys.exit(1)

if settings.args.playlist:
    search_results = search_playlist_videos(settings.args.playlist, settings.env["api_key"], settings.args.results)
    handle_error(search_results.get("error"))
    video_ids = [video["contentDetails"]["videoId"] for video in search_results.get("items", [])]
else:
    search_results = search_videos(settings.args.channel, settings.env["api_key"], settings.args.results)
    handle_error(search_results.get("error"))
    video_ids = [video["id"]["videoId"] for video in search_results.get("items", [])]

videos = video_details(video_ids, settings.env["api_key"])
handle_error(videos.get("error"))

videos = video_info(videos)

if settings.args.output:
    fg = generate_fg(
        feed_id="https://www.youtube.com/channel/" + settings.args.channel,
        title="Youtube Search",
        subtitle="Youtube Search",
        link="https://www.youtube.com/channel/" + settings.args.channel,
        language="en",
    )
    if settings.args.timezone:
        generate_video_rss(videos, fg, settings.args.output, settings.args.timezone)
    else:
        generate_video_rss(videos, fg, settings.args.output)
else:
    print(videos)
