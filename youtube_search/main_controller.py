"""Main controller for Youtube search"""

from youtube_search.feed_generator import generate_fg, generate_video_rss
from youtube_search.playlist import get_playlist_id
from youtube_search.search_videos import search_playlist_videos, search_videos
from youtube_search.video_details import video_details, video_info

class MainController:
    """Main controller for Youtube search"""
    def get_playlist(self, settings) -> None:
        """Get the playlist ID for a channel's uploads"""
        response = get_playlist_id(settings.args.get_playlist, settings.env["api_key"])
        data = response.json()
        uploads_playlist_id = data["items"][0]["contentDetails"]["relatedPlaylists"][
            "uploads"
        ]
        print(f"The playlist ID for the channel uploads is: {uploads_playlist_id}")

    def get_videos(self, settings):
        """Get the videos for a channel or playlist"""
        if settings.args.get_playlist != None:
            search_results = search_playlist_videos(
                settings.args.playlist, settings.env["api_key"], settings.args.results
            )
            video_ids = [
                video["contentDetails"]["videoId"]
                for video in search_results.get("items", [])
            ]
        else:
            search_results = search_videos(
                settings.args.channel, settings.env["api_key"], settings.args.results
            )
            video_ids = [
                video["id"]["videoId"] for video in search_results.get("items", [])
            ]
        videos = video_details(video_ids, settings.env["api_key"])
        videos = video_info(videos)
        return videos

    def generate_rss(self, settings, videos):
        """Generate the RSS feed"""
        fg = generate_fg(
            feed_id="https://www.youtube.com/channel/" + settings.args.channel,
            title="Youtube Search",
            subtitle="Youtube Search",
            link="https://www.youtube.com/channel/" + settings.args.channel,
            language="en",
        )
        generate_video_rss(
            videos,
            fg,
            settings.args.output,
            settings.args.timezone if settings.args.timezone else None,
        )
