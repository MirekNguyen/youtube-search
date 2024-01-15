"""Get the playlist id of a channel"""
import requests

from youtube_search.yt_api_exception import YoutubeAPIError

CHANNEL_URL = "https://www.googleapis.com/youtube/v3/channels"


def get_playlist_id(channel_id, api_key):
    """Get the playlist id of a channel"""
    params = {"part": "contentDetails", "id": channel_id, "key": api_key}
    response = requests.get(CHANNEL_URL, params=params, timeout=5)
    if response.status_code != 200:
        error_message = response.json()["error"]['message']
        status_code = response.status_code
        raise YoutubeAPIError(
            f"Error throwed by the API ({status_code}): {error_message}"
        )
    return response
