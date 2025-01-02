from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field

from xclient.models.tweet import ItemResult
from xclient.models.user import UserResults


class InstructionType(str, Enum):
    TimelineAddEntries = "TimelineAddEntries"
    TimelineAddToModule = "TimelineAddToModule"
    TimelineClearCache = "TimelineClearCache"
    TimelinePinEntry = "TimelinePinEntry"
    TimelineReplaceEntry = "TimelineReplaceEntry"
    TimelineShowAlert = "TimelineShowAlert"
    TimelineTerminateTimeline = "TimelineTerminateTimeline"
    TimelineShowCover = "TimelineShowCover"


class ContentEntryType(str, Enum):
    TimelineTimelineItem = "TimelineTimelineItem"
    TimelineTimelineCursor = "TimelineTimelineCursor"
    TimelineTimelineModule = "TimelineTimelineModule"


class CursorType(str, Enum):
    Top = "Top"
    Bottom = "Bottom"
    ShowMore = "ShowMore"
    ShowMoreThreads = "ShowMoreThreads"
    Gap = "Gap"
    ShowMoreThreadsPrompt = "ShowMoreThreadsPrompt"


class DisplayType(str, Enum):
    Vertical = "Vertical"
    VerticalConversation = "VerticalConversation"
    VerticalGrid = "VerticalGrid"
    Carousel = "Carousel"


class ContentItemType(str, Enum):
    TimelineTweet = "TimelineTweet"
    TimelineTimelineCursor = "TimelineTimelineCursor"
    TimelineUser = "TimelineUser"
    TimelinePrompt = "TimelinePrompt"
    TimelineMessagePrompt = "TimelineMessagePrompt"
    TimelineCommunity = "TimelineCommunity"


class ClientEventInfo(BaseModel):
    component: Optional[str] = None
    element: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class DisplayTreatment(BaseModel):
    action_text: str = Field(alias="actionText")
    label_text: Optional[str] = Field(default=None, alias="labelText")


class TimelineTimelineCursor(BaseModel):
    entry_type: Optional[ContentEntryType] = Field(default=None, alias="entryType")
    item_type: Optional[ContentEntryType] = Field(default=None, alias="itemType")
    cursor_type: CursorType = Field(alias="cursorType")
    value: str
    stop_on_empty_response: Optional[bool] = Field(
        default=None, alias="stopOnEmptyResponse"
    )
    display_treatment: Optional[DisplayTreatment] = Field(
        default=None, alias="displayTreatment"
    )


class SocialContextLandingUrl(BaseModel):
    url_type: Literal["DeepLink", "UrtEndpoint", "ExternalUrl"] = Field(alias="urlType")
    url: str
    urt_endpoint_options: Optional["UrtEndpointOptions"] = Field(
        default=None, alias="urtEndpointOptions"
    )


class UrtEndpointRequestParams(BaseModel):
    key: str
    value: str


class UrtEndpointOptions(BaseModel):
    title: str
    request_params: List[UrtEndpointRequestParams] = Field(alias="requestParams")


class TopicContext(BaseModel):
    id: Optional[str] = None
    topic_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    icon_url: Optional[str] = None
    following: Optional[bool] = None
    not_interested: Optional[bool] = None


class TimelineGeneralContext(BaseModel):
    type: str
    context_type: Literal[
        "Follow",
        "Pin",
        "Like",
        "Location",
        "Sparkle",
        "Conversation",
        "List",
        "Community",
    ] = Field(alias="contextType")
    text: Optional[str] = None
    landing_url: Optional[SocialContextLandingUrl] = Field(
        default=None, alias="landingUrl"
    )


class TimelineTopicContext(BaseModel):
    type: str
    topic: TopicContext
    functionality_type: Literal["Basic"] = Field(alias="functionalityType")


SocialContextUnion = Union[TimelineGeneralContext, TimelineTopicContext]


class TextHighlight(BaseModel):
    start_index: int = Field(alias="startIndex")
    end_index: int = Field(alias="endIndex")


class Highlight(BaseModel):
    text_highlights: List[TextHighlight] = Field(alias="textHighlights")


class TimelineTweet(BaseModel):
    item_type: ContentItemType = Field(alias="itemType")
    tweet_display_type: Literal[
        "Tweet", "SelfThread", "MediaGrid", "CondensedTweet"
    ] = Field(alias="tweetDisplayType")
    tweet_results: "ItemResult" = Field(alias="tweet_results")
    social_context: Optional[SocialContextUnion] = Field(
        default=None, alias="socialContext"
    )
    promoted_metadata: Optional[Dict[str, Any]] = Field(
        default=None, alias="promotedMetadata"
    )
    highlights: Optional[Highlight] = None


class TimelineUser(BaseModel):
    item_type: ContentItemType = Field(alias="itemType")
    social_context: Optional[SocialContextUnion] = Field(
        default=None, alias="socialContext"
    )
    user_display_type: Literal["User", "UserDetailed", "SubscribableUser"] = Field(
        alias="userDisplayType"
    )
    user_results: "UserResults"


class FeedbackInfo(BaseModel):
    feedback_type: str = Field(alias="feedbackType")
    feedback_keys: Optional[List[str]] = Field(default=None, alias="feedbackKeys")


class ModuleEntry(BaseModel):
    client_event_info: Optional[ClientEventInfo] = Field(
        default=None, alias="clientEventInfo"
    )
    item_content: "ItemContentUnion" = Field(alias="itemContent")
    feedback_info: Optional[FeedbackInfo] = Field(default=None, alias="feedbackInfo")


class ModuleItem(BaseModel):
    entry_id: str = Field(alias="entryId")
    item: ModuleEntry


class TimelineTimelineModule(BaseModel):
    entry_type: ContentEntryType = Field(alias="entryType")
    display_type: DisplayType = Field(alias="displayType")
    items: Optional[List[ModuleItem]] = None
    footer: Optional[Dict[str, Any]] = None
    header: Optional[Dict[str, Any]] = None
    client_event_info: Dict[str, Any] = Field(alias="clientEventInfo")
    metadata: Optional[Dict[str, Any]] = None
    feedback_info: Optional[FeedbackInfo] = Field(default=None, alias="feedbackInfo")


class TimelineTimelineItem(BaseModel):
    entry_type: ContentEntryType = Field(alias="entryType")
    item_content: "ItemContentUnion" = Field(alias="itemContent")
    client_event_info: Optional[ClientEventInfo] = Field(
        default=None, alias="clientEventInfo"
    )
    feedback_info: Optional[FeedbackInfo] = Field(default=None, alias="feedbackInfo")


class TimelineAddEntry(BaseModel):
    content: "ContentUnion"
    entry_id: str = Field(alias="entryId")
    sort_index: str = Field(alias="sortIndex")


class TimelineAddEntries(BaseModel):
    type: Literal[InstructionType.TimelineAddEntries]
    entries: List[TimelineAddEntry]


class TimelineAddToModule(BaseModel):
    type: Literal[InstructionType.TimelineAddToModule]
    module_items: List[ModuleItem] = Field(alias="moduleItems")
    module_entry_id: str = Field(alias="moduleEntryId")
    prepend: Optional[bool] = None


class TimelineClearCache(BaseModel):
    type: Literal[InstructionType.TimelineClearCache]


class TimelinePinEntry(BaseModel):
    type: Literal[InstructionType.TimelinePinEntry]
    entry: TimelineAddEntry


class TimelineReplaceEntry(BaseModel):
    type: Literal[InstructionType.TimelineReplaceEntry]
    entry_id_to_replace: str
    entry: TimelineAddEntry


class TimelineShowAlert(BaseModel):
    type: Literal[InstructionType.TimelineShowAlert]
    alert_type: Optional[Literal["NewTweets"]] = Field(default=None, alias="alertType")
    trigger_delay_ms: Optional[int] = Field(default=None, alias="triggerDelayMs")
    display_duration_ms: Optional[int] = Field(default=None, alias="displayDurationMs")
    users_results: List["UserResults"] = Field(alias="usersResults")
    rich_text: Dict[str, Any] = Field(alias="richText")
    icon_display_info: Optional[Dict[str, Any]] = Field(
        default=None, alias="iconDisplayInfo"
    )
    color_config: Optional[Dict[str, Any]] = Field(default=None, alias="colorConfig")
    display_location: Optional[Literal["Top"]] = Field(
        default=None, alias="displayLocation"
    )


class TimelineTerminateTimeline(BaseModel):
    type: Literal[InstructionType.TimelineTerminateTimeline]
    direction: Literal["Top", "Bottom", "TopAndBottom"]


InstructionUnion = Union[
    TimelineAddEntries,
    TimelineAddToModule,
    TimelineClearCache,
    TimelinePinEntry,
    TimelineReplaceEntry,
    TimelineShowAlert,
    TimelineTerminateTimeline,
]


class Timeline(BaseModel):
    instructions: List[InstructionUnion]
    metadata: Optional[Dict[str, Any]] = None
    response_objects: Optional[Dict[str, Any]] = Field(
        default=None, alias="responseObjects"
    )


class TimelineV2(BaseModel):
    timeline: Optional[Timeline] = None


ItemContentUnion = Union[TimelineTweet, TimelineTimelineCursor, TimelineUser]
ContentUnion = Union[
    TimelineTimelineItem, TimelineTimelineModule, TimelineTimelineCursor
]
