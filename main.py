"""Youtube Search"""
import sys

from youtube_search.main_controller import MainController
from youtube_search.settings import Settings

try:
    controller = MainController()
    settings = Settings()
    if not settings.env["api_key"]:
        raise Exception("Invalid or non-existent Youtube API key")
    if (
        not settings.args.channel
        and not settings.args.playlist
        and not settings.args.get_playlist
    ):
        raise Exception("Please specify a channel or playlist ID")

    if settings.args.get_playlist:
        controller.get_playlist(settings)
        sys.exit(0)
    else:
        videos = controller.get_videos(settings)

    if settings.args.output:
        controller.generate_rss(settings, videos)
    else:
        print(videos)
except Exception as e:
    print(e)
    sys.exit(1)
