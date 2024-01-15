"""Settings for youtube_search"""

import argparse
import os
from dotenv import load_dotenv


class Settings:
    """Settings for youtube_search"""
    def __init__(self) -> None:
        self.args = self.parse_args()
        self.env = self.load_env()
    def parse_args(self):
        """Parse arguments"""
        parser = argparse.ArgumentParser(description="Youtube Search")
        parser.add_argument(
            "-c", "--channel", action="store", help="Channel ID (required)"
        )
        parser.add_argument(
            "-r", "--results", action="store", help="Number of results", default=1
        )
        parser.add_argument("-o", "--output", action="store", help="Generate RSS feed")
        parser.add_argument("-t", "--timezone", action="store", help="Timezone")
        parser.add_argument("-p", "--playlist", action="store", help="Playlist ID")
        parser.add_argument(
            "--get-playlist", action="store", help="Get playlist ID from channel ID"
        )
        args = parser.parse_args()
        return args

    def load_env(self):
        """Load environment variables"""
        load_dotenv()
        api_key = os.environ.get(
            "YOUTUBE_DATA_API_KEY", os.getenv("YOUTUBE_DATA_API_KEY")
        )
        env = {"api_key": api_key}
        return env
