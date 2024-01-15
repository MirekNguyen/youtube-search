"""Exception for Youtube API errors."""

class YoutubeAPIError(Exception):
    """Exception for Youtube API errors."""
    def __init__(self, message):
        super().__init__(message)
