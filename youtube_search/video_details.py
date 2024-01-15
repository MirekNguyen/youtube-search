"""This module is used to search for the get the details of the videos."""
from datetime import datetime

import requests
from isodate import parse_duration

from youtube_search.yt_api_exception import YoutubeAPIError

VIDEO_DETAILS_URL = "https://www.googleapis.com/youtube/v3/videos?"


def video_details(video_ids, api_key):
    """This function is used to get the details of the videos."""
    video_params = {
        "part": "snippet,contentDetails,liveStreamingDetails",
        "id": ",".join(video_ids),
        "key": api_key,
    }
    response = requests.get(VIDEO_DETAILS_URL, params=video_params, timeout=5)
    if response.status_code != 200:
        error_message = response.json()["error"]["message"]
        status_code = response.status_code
        raise YoutubeAPIError(f"Error throwed by the API ({status_code}): {error_message}")
    videos = response.json()
    return videos


def video_info(videos):
    """This function is used to get the details of the videos."""
    video_items = videos.get("items", [])
    video_objects = list(
        map(
            lambda video: {
                "title": video["snippet"]["title"],
                "id": video["id"],
                "description": video["snippet"]["description"],
                "livestream": video.get("liveStreamingDetails") is not None,
                "duration": parse_duration(
                    video["contentDetails"]["duration"]
                ).total_seconds(),
                "is_short": is_short(
                    parse_duration(video["contentDetails"]["duration"]).total_seconds()
                ),
                "published_at": datetime.strptime(
                    video["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"
                ),
            },
            video_items,
        )
    )
    return video_objects


def is_short(duration):
    """This function is used to check if the video is short."""
    return duration <= 61


def print_video_details(videos):
    """This function is used to print the details of the videos."""
    for video in videos:
        print(
            f"{video['title']}-{video['duration']}-{video['is_short']}-{video['published_at']}"
        )
