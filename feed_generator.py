"""This module is used to generate the RSS feed."""
import pytz
from feedgen.feed import FeedGenerator


def generate_fg(feed_id, title, subtitle, link, language="en"):
    """This function is used to generate the RSS feed."""
    fg = FeedGenerator()
    fg.id(feed_id)
    fg.title(title)
    fg.subtitle(subtitle)
    fg.link(href=link, rel="self")
    fg.language(language)
    return fg


def generate_video_rss(videos, fg, file, timezone="Etc/UTC"):
    """This function is used to generate the RSS feed."""
    videos = sorted(videos, key=lambda video: video["published_at"])
    timezone = pytz.timezone(timezone)
    for video in videos:
        if video["liveBroadcastContent"] or video["is_short"]:
            continue
        link = "https://www.youtube.com/watch?v=" + video["id"]
        fe = fg.add_entry()
        fe.id(link)
        fe.title(video["title"])
        fe.link(href=link, replace=True)
        fe.description(
            link
            + "<br>"
            + "Published at:"
            + str(video["published_at"])
            + "<br>"
            + "Video duration: "
            + str(video["duration"])
            + "<br>"
            + "Description: "
            + video["description"]
        )
        fe.pubDate(timezone.localize(video["published_at"]))
    fg.rss_str(pretty=True)
    fg.rss_file(file)
