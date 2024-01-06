"""This module is used to search for the latest video of a channel on YouTube."""
import requests

BASE_VIDEO_URL = "https://www.googleapis.com/youtube/v3/search?"
BASE_VIDEO_PLAYLIST_URL = "https://www.googleapis.com/youtube/v3/playlistItems"

def search_videos(channel_id, api_key, max_results = 1):
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
    return response.json()

def search_playlist_videos(playlist_id, api_key, max_results = 1):
    """Search for the latest video of a channel on YouTube."""
    params = {
        'part': 'contentDetails',
        'playlistId': playlist_id,
        'maxResults': max_results,
        'key': api_key
    }
    response = requests.get(BASE_VIDEO_PLAYLIST_URL, params=params, timeout=5)
    return response.json()
