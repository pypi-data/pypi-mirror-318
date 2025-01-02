from pydantic import BaseModel


class FavoriteResult(BaseModel):
    """Represents the result of a favorite/unfavorite action."""

    favorite_tweet: str | None = None
    unfavorite_tweet: str | None = None


class RetweetResult(BaseModel):
    """Represents the result of a retweet/unretweet action."""

    rest_id: str
    full_text: str
