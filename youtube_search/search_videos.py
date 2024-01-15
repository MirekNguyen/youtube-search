"""This module is used to search for the latest video of a channel on YouTube."""
import requests

from youtube_search.yt_api_exception import YoutubeAPIError

BASE_VIDEO_URL = "https://www.googleapis.com/youtube/v3/search?"
BASE_VIDEO_PLAYLIST_URL = "https://www.googleapis.com/youtube/v3/playlistItems"


def search_videos(channel_id, api_key, max_results=1):
    """Search for the latest video of a channel on YouTube."""
    params = {
        "part": "id",
        "channelId": channel_id,
        "maxResults": max_results,
        "order": "date",
        "type": "video",
        "key": api_key,
    }
    response = requests.get(BASE_VIDEO_URL, params=params, timeout=5)
    if response.status_code != 200:
        error_message = response.json()["error"]["message"]
        status_code = response.status_code
        raise YoutubeAPIError(f"Error throwed by the API ({status_code}): {error_message}")
    return response.json()


def search_playlist_videos(playlist_id, api_key, max_results=1):
    """Search for the latest video of a channel on YouTube."""
    params = {
        "part": "contentDetails",
        "playlistId": playlist_id,
        "maxResults": max_results,
        "key": api_key,
    }
    response = requests.get(BASE_VIDEO_PLAYLIST_URL, params=params, timeout=5)
    if response.status_code != 200:
        error_message = response.json()["error"]["message"]
        status_code = response.status_code
        raise YoutubeAPIError(f"Error throwed by the API ({status_code}): {error_message}")
    return response.json()
