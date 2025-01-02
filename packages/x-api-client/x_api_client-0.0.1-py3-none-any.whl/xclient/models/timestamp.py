from typing import List

from pydantic import BaseModel


class Timestamp(BaseModel):
    """
    Model representing a timestamp in a tweet.
    Used for video timestamps that can be clicked to jump to specific points in videos.
    """

    indices: List[int]  # The position of the timestamp in the tweet text
    seconds: int  # The number of seconds into the video
    text: str  # The display text of the timestamp (e.g. "1:30")
