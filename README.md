# Youtube Search

This project is a command-line application that allows you to search for videos on a specific YouTube channel.

## Requirements

- Python 3.6+

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use this application, you need to provide a YouTube Data API key and the ID of the YouTube channel you want to search.

You can provide the API key by setting the `YOUTUBE_DATA_API_KEY` environment variable. You can do this in a `.env` file in the root directory of the project.

The channel ID can be provided as a command-line argument:

```bash
python main.py --channel CHANNEL_ID
```

You can also specify the number of search results you want to get (the default is 1):

```bash
python main.py --channel CHANNEL_ID --results NUMBER_OF_RESULTS
```

## Modules

- `search_videos`: This module is responsible for searching videos on a specific YouTube channel.
- `video_details`: This module is responsible for getting the details of a specific video.

## Error Handling

The application will exit with an error message if:
- The channel ID is not provided.
- The API key is not set or is invalid.
- There is an error while fetching the search results or video details.
