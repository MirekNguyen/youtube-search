import os

import requests
from dotenv import load_dotenv
import argparse

parser = argparse.ArgumentParser(description="Youtube Search")
parser.add_argument("-c", "--channel", action="store", help="Channel ID (required)")

args = parser.parse_args()

if not args.channel:
    print("Please specify a channel ID")
    exit(1)

load_dotenv()
api_key = os.getenv("YOUTUBE_DATA_API_KEY")

