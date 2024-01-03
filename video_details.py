"""This module is used to search for the get the details of the videos."""
import requests

VIDEO_DETAILS_URL = "https://www.googleapis.com/youtube/v3/videos?"

def video_details(video_ids, api_key):
    """This function is used to get the details of the videos."""
    video_params = {
        "part": "snippet,contentDetails",
        "id": ",".join(video_ids),
        "key": api_key,
    }
    video_response = requests.get(VIDEO_DETAILS_URL, params=video_params, timeout=5)
    videos = video_response.json()
    return videos

def print_video_details(videos):
    """This function is used to print the details of the videos."""
    for video in videos.get("items", []):
        title = video["snippet"]["title"]
        duration = video["contentDetails"]["duration"]
        print(f"{title} - {duration}")
