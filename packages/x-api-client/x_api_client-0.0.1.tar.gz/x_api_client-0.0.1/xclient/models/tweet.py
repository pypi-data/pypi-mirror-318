from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field, HttpUrl

from xclient.models.timestamp import Timestamp
from xclient.models.user import UserResultCore


class TweetInterstitialText(BaseModel):
    rtl: bool
    text: str
    entities: List["TweetInterstitialTextEntity"]


class TweetInterstitialTextEntityRef(BaseModel):
    type: Literal["TimelineUrl"]
    url: HttpUrl
    url_type: Literal["ExternalUrl"] = Field(alias="urlType")


class TweetInterstitialTextEntity(BaseModel):
    from_index: int = Field(alias="fromIndex")
    to_index: int = Field(alias="toIndex")
    ref: TweetInterstitialTextEntityRef


class TweetInterstitialRevealText(BaseModel):
    rtl: bool
    text: str
    entities: List[TweetInterstitialTextEntity]


class TweetInterstitial(BaseModel):
    display_type: Literal["NonCompliant"] = Field(alias="displayType")
    text: TweetInterstitialText
    reveal_text: TweetInterstitialRevealText = Field(alias="revealText")


class MediaVisibilityResultsBlurredImageInterstitial(BaseModel):
    opacity: float
    text: TweetInterstitialText
    title: TweetInterstitialText


class MediaVisibilityResults(BaseModel):
    blurred_image_interstitial: MediaVisibilityResultsBlurredImageInterstitial


class TweetWithVisibilityResults(BaseModel):
    tweet: "Tweet"
    limited_action_results: Optional[Dict[str, Any]] = Field(
        default=None, alias="limitedActionResults"
    )
    tweet_interstitial: Optional[TweetInterstitial] = Field(
        default=None, alias="tweetInterstitial"
    )
    media_visibility_results: Optional[MediaVisibilityResults] = Field(
        default=None, alias="mediaVisibilityResults"
    )


class TweetTombstone(BaseModel):
    pass  # Placeholder for now


class TweetUnavailable(BaseModel):
    reason: str


class NoteTweetResultRichTextTag(BaseModel):
    from_index: int
    to_index: int
    richtext_types: List[Literal["Bold", "Italic"]]


class NoteTweetResultRichText(BaseModel):
    richtext_tags: List[NoteTweetResultRichTextTag]


class NoteTweetResultMediaInlineMedia(BaseModel):
    media_id: str
    index: int


class NoteTweetResultMedia(BaseModel):
    inline_media: List[NoteTweetResultMediaInlineMedia]


class NoteTweetResultData(BaseModel):
    entity_set: "Entities"  # Forward reference
    id: str
    text: str
    media: Optional[NoteTweetResultMedia] = None
    richtext: Optional[NoteTweetResultRichText] = None


class NoteTweetResult(BaseModel):
    result: NoteTweetResultData


class NoteTweet(BaseModel):
    is_expandable: bool
    note_tweet_results: NoteTweetResult


class TweetEditControlInitial(BaseModel):
    edit_tweet_ids: List[str]
    editable_until_msecs: str
    is_edit_eligible: bool
    edits_remaining: str


class TweetEditControl(BaseModel):
    edit_tweet_ids: List[str]
    editable_until_msecs: str
    is_edit_eligible: bool
    edits_remaining: str
    initial_tweet_id: Optional[str] = None
    edit_control_initial: Optional[TweetEditControlInitial] = None


class TweetEditPrespective(BaseModel):
    favorited: Optional[bool] = None
    retweeted: Optional[bool] = None


class TweetView(BaseModel):
    count: Optional[str] = None
    state: Literal["Enabled", "EnabledWithCount"]


class UnifiedCard(BaseModel):
    card_fetch_state: Literal["NoCard"]


class TweetPreviousCounts(BaseModel):
    bookmark_count: int
    favorite_count: int
    quote_count: int
    reply_count: int
    retweet_count: int


class SuperFollowsReplyUserResultLegacy(BaseModel):
    screen_name: str


class SuperFollowsReplyUserResultData(BaseModel):
    legacy: SuperFollowsReplyUserResultLegacy


class SuperFollowsReplyUserResult(BaseModel):
    result: SuperFollowsReplyUserResultData


class CommunityUrls(BaseModel):
    permalink: "CommunityUrlsPermalink"


class CommunityUrlsPermalink(BaseModel):
    url: HttpUrl


class CommunityRule(BaseModel):
    rest_id: str
    name: str
    description: Optional[str]


class CommunityJoinActionResult(BaseModel):
    pass  # Placeholder for now


class CommunityJoinActionUnavailable(BaseModel):
    reason: Literal["ViewerRequestRequired"]
    message: str


CommunityJoinActionUnion = Union[
    CommunityJoinActionResult, CommunityJoinActionUnavailable
]


class CommunityActions(BaseModel):
    delete_action_result: Optional[Dict[str, Any]] = None
    join_action_result: Optional[CommunityJoinActionUnion] = None
    leave_action_result: Optional[Dict[str, Any]] = None
    pin_action_result: Optional[Dict[str, Any]] = None
    unpin_action_result: Optional[Dict[str, Any]] = None


class CommunityRelationship(BaseModel):
    id: str
    rest_id: str
    moderation_state: Dict[str, Any]
    actions: CommunityActions


class PrimaryCommunityTopic(BaseModel):
    topic_id: str
    topic_name: str


class Entities(BaseModel):
    hashtags: List[Dict[str, Any]]  # Simplified for now
    symbols: List[Dict[str, Any]]  # Simplified for now
    user_mentions: List[Dict[str, Any]]  # Simplified for now
    urls: List["Url"]
    media: Optional[List["Media"]] = None
    timestamps: Optional[List["Timestamp"]] = None


class Url(BaseModel):
    display_url: str
    expanded_url: HttpUrl
    url: HttpUrl
    indices: List[int]


class MediaSize(BaseModel):
    w: int
    h: int
    resize: Literal["crop", "fit"]


class MediaSizes(BaseModel):
    large: MediaSize
    medium: MediaSize
    small: MediaSize
    thumb: MediaSize


class MediaVideoInfoVariant(BaseModel):
    bitrate: Optional[int] = None
    content_type: str
    url: HttpUrl


class MediaVideoInfo(BaseModel):
    aspect_ratio: List[int]
    duration_millis: Optional[int] = None
    variants: List[MediaVideoInfoVariant]


class MediaOriginalInfo(BaseModel):
    height: int
    width: int
    focus_rects: Optional[List[Dict[str, int]]] = None


class ExtMediaAvailability(BaseModel):
    status: Optional[Literal["Available", "Unavailable"]] = None
    reason: Optional[str] = None


class SensitiveMediaWarning(BaseModel):
    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None


class Media(BaseModel):
    display_url: HttpUrl
    expanded_url: HttpUrl
    id_str: str
    indices: List[int]
    media_url_https: HttpUrl
    type: Literal["photo", "video", "animated_gif"]
    url: HttpUrl
    features: Optional[Dict[str, Any]]
    sizes: MediaSizes
    original_info: MediaOriginalInfo
    media_key: str
    ext_media_availability: ExtMediaAvailability
    video_info: Optional[MediaVideoInfo] = None
    sensitive_media_warning: Optional[SensitiveMediaWarning] = None


class TweetCardLegacyBindingValueDataImage(BaseModel):
    height: int
    width: int
    url: HttpUrl
    alt: Optional[str] = None


class UserValue(BaseModel):
    id_str: str


class TweetCardLegacyBindingValueData(BaseModel):
    string_value: Optional[str] = None
    type: str
    boolean_value: Optional[bool] = None
    scribe_key: Optional[str] = None
    image_value: Optional[TweetCardLegacyBindingValueDataImage] = None
    image_color_value: Optional[Dict[str, Any]] = None
    user_value: Optional[UserValue] = None


class TweetCardLegacyBindingValue(BaseModel):
    key: str
    value: TweetCardLegacyBindingValueData


class TweetCardPlatform(BaseModel):
    audience: Dict[str, str]
    device: Dict[str, str]


class TweetCardLegacy(BaseModel):
    binding_values: List[TweetCardLegacyBindingValue]
    card_platform: Optional[Dict[str, Any]] = None
    name: str
    url: str
    user_refs_results: Optional[List[Dict[str, Any]]] = None


class TweetCard(BaseModel):
    rest_id: Optional[str] = None
    legacy: Optional[TweetCardLegacy] = None


class TweetLegacy(BaseModel):
    bookmark_count: int
    bookmarked: bool
    created_at: str
    conversation_id_str: str
    display_text_range: List[int]
    entities: Entities
    favorite_count: int
    favorited: bool
    full_text: str
    is_quote_status: bool
    lang: str
    quote_count: int
    reply_count: int
    retweet_count: int
    retweeted: bool
    user_id_str: str
    id_str: str
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None
    self_thread: Optional[Dict[str, str]] = None
    scopes: Optional[Dict[str, bool]] = None
    retweeted_status_result: Optional[Dict[str, Any]] = None
    quoted_status_permalink: Optional[Dict[str, str]] = None
    quoted_status_id_str: Optional[str] = None


class Tweet(BaseModel):
    rest_id: str
    has_birdwatch_notes: Optional[bool] = None
    core: Optional["UserResultCore"] = None
    edit_control: Optional[TweetEditControl] = None
    edit_perspective: Optional[TweetEditPrespective] = None
    is_translatable: Optional[bool] = None
    views: Optional[TweetView] = None
    source: Optional[str] = None
    legacy: Optional[TweetLegacy] = None
    quick_promote_eligibility: Optional[Dict[str, Any]] = None
    card: Optional[TweetCard] = None
    unified_card: Optional[UnifiedCard] = None
    quoted_status_result: Optional[Dict[str, Any]] = None
    note_tweet: Optional[NoteTweet] = None


TweetUnion = Union[Tweet, TweetWithVisibilityResults, TweetTombstone, TweetUnavailable]


class ItemResult(BaseModel):
    result: Optional[TweetUnion] = None


class MediaEntity(BaseModel):
    """Model for a media entity in a tweet."""

    media_id: str
    tagged_users: Optional[List[str]] = None
    alt_text: Optional[str] = None


class CreateTweetMedia(BaseModel):
    """Model for media attachments in a tweet."""

    media_entities: List[MediaEntity] = Field(default_factory=list)
    possibly_sensitive: bool = False


class CreateTweetVariables(BaseModel):
    """Model for tweet creation parameters."""

    tweet_text: str
    dark_request: bool = False
    media: Optional[CreateTweetMedia] = None
    semantic_annotation_ids: List[str] = Field(default_factory=list)
    disallowed_reply_options: Optional[List[str]] = None
    reply: Optional[Dict[str, Any]] = None
    quote_tweet_id: Optional[str] = None


class DeleteTweetResult(BaseModel):
    """Response model for tweet deletion."""

    tweet_results: dict = {}
