"""Get the playlist id of a channel"""
import requests

CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/channels'
def get_playlist_id(channel_id, api_key):
    """Get the playlist id of a channel"""
    params = {
        'part': 'contentDetails',
        'id': channel_id,
        'key': api_key
    }
    response = requests.get(CHANNEL_URL, params=params, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Error throwed by the API ({response.status_code}): {response.json()['error']['message']}")
    return response
