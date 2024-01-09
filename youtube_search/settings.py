"""Settings for youtube_search"""

import argparse
import os

from dotenv import load_dotenv


class Settings:
    def parse_args(self) -> bool:
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
        self.args = parser.parse_args()
        return True

    def load_env(self) -> bool:
        load_dotenv()
        api_key = os.environ.get(
            "YOUTUBE_DATA_API_KEY", os.getenv("YOUTUBE_DATA_API_KEY")
        )
        self.env = {
            "api_key": api_key
        }
        return True
