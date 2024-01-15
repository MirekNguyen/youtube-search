"""Youtube Search"""
import sys

from youtube_search.main_controller import MainController
from youtube_search.settings import Settings
from youtube_search.yt_api_exception import YoutubeAPIError

try:
    controller = MainController()
    settings = Settings()
    if not settings.env["api_key"]:
        raise EnvironmentError("Invalid or non-existent Youtube API key")

    if settings.args.get_channel:
        controller.get_channel(settings)
        sys.exit(0)
    if settings.args.get_playlist:
        controller.get_playlist(settings)
        sys.exit(0)
    if not settings.args.channel:
        raise EnvironmentError("Please specify a channel")

    videos = controller.get_videos(settings)

    if settings.args.output:
        controller.generate_rss(settings, videos)
    else:
        print(videos)

except (EnvironmentError, YoutubeAPIError) as e:
    print(e)
    sys.exit(1)
