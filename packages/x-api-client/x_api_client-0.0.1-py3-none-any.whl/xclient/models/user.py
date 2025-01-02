from typing import List, Literal, Optional, Union

from pydantic import BaseModel, HttpUrl


class UserProfessionalCategory(BaseModel):
    id: int
    name: str
    icon_name: str


class UserProfessional(BaseModel):
    rest_id: str
    professional_type: Literal["Business", "Creator"]
    category: List[UserProfessionalCategory]


class UserVerificationInfoReasonDescriptionEntitiesRef(BaseModel):
    url: HttpUrl
    url_type: Literal["ExternalUrl"]


class UserVerificationInfoReasonDescriptionEntities(BaseModel):
    from_index: int
    to_index: int
    ref: UserVerificationInfoReasonDescriptionEntitiesRef


class UserVerificationInfoReasonDescription(BaseModel):
    text: str
    entities: List[UserVerificationInfoReasonDescriptionEntities]


class UserVerificationInfoReason(BaseModel):
    description: UserVerificationInfoReasonDescription
    verified_since_msec: str
    override_verified_year: Optional[int] = None


class UserVerificationInfo(BaseModel):
    is_identity_verified: bool
    reason: Optional[UserVerificationInfoReason] = None


class UserHighlightsInfo(BaseModel):
    can_highlight_tweets: bool
    highlighted_tweets: str


class UserTipJarSettings(BaseModel):
    is_enabled: Optional[bool] = None
    patreon_handle: Optional[str] = None
    bitcoin_handle: Optional[str] = None
    ethereum_handle: Optional[str] = None
    cash_app_handle: Optional[str] = None
    venmo_handle: Optional[str] = None
    gofundme_handle: Optional[str] = None
    bandcamp_handle: Optional[str] = None


class UserLegacyExtendedProfileBirthdate(BaseModel):
    day: int
    month: int
    year: int
    visibility: Literal["Self", "Public", "MutualFollow", "Followers", "Following"]
    year_visibility: Literal["Self", "Public", "MutualFollow", "Followers", "Following"]


class UserLegacyExtendedProfile(BaseModel):
    birthdate: Optional[UserLegacyExtendedProfileBirthdate] = None


class UserLegacy(BaseModel):
    blocked_by: Optional[bool] = None
    blocking: Optional[bool] = None
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
    created_at: str  # TODO: Use datetime with custom formatter
    default_profile: bool
    default_profile_image: bool
    description: str
    entities: dict  # TODO: Define proper entity types
    fast_followers_count: int
    favourites_count: int
    follow_request_sent: Optional[bool] = None
    followed_by: Optional[bool] = None
    followers_count: int
    following: Optional[bool] = None
    friends_count: int
    has_custom_timelines: bool
    is_translator: bool
    listed_count: int
    location: str
    media_count: int
    muting: Optional[bool] = None
    name: str
    normal_followers_count: int
    notifications: Optional[bool] = None
    pinned_tweet_ids_str: List[str]
    possibly_sensitive: bool
    profile_banner_extensions: Optional[dict] = None
    profile_banner_url: Optional[HttpUrl] = None
    profile_image_extensions: Optional[dict] = None
    profile_image_url_https: HttpUrl
    profile_interstitial_type: str
    protected: Optional[bool] = None
    screen_name: str
    statuses_count: int
    translator_type: str
    url: Optional[str] = None
    verified: bool
    want_retweets: Optional[bool] = None
    verified_type: Optional[Literal["Business", "Government"]] = None
    withheld_in_countries: Optional[List[str]] = None


class User(BaseModel):
    affiliates_highlighted_label: dict
    has_graduated_access: Optional[bool] = None
    has_nft_avatar: Optional[bool] = None
    id: str
    is_blue_verified: bool
    legacy: UserLegacy
    rest_id: str
    business_account: Optional[dict] = None
    super_follow_eligible: Optional[bool] = None
    super_followed_by: Optional[bool] = None
    super_following: Optional[bool] = None
    profile_image_shape: Literal["Circle", "Square", "Hexagon"]
    professional: Optional[UserProfessional] = None
    user_seed_tweet_count: Optional[int] = None
    highlights_info: Optional[UserHighlightsInfo] = None
    creator_subscriptions_count: Optional[int] = None
    verification_info: Optional[UserVerificationInfo] = None
    is_profile_translatable: Optional[bool] = None
    tipjar_settings: Optional[UserTipJarSettings] = None
    legacy_extended_profile: Optional[UserLegacyExtendedProfile] = None
    has_hidden_likes_on_profile: Optional[bool] = None
    premium_gifting_eligible: Optional[bool] = None


class UserUnavailable(BaseModel):
    reason: str
    message: Optional[str] = None


class UserResults(BaseModel):
    result: Union[User, UserUnavailable]


class UserResultCore(BaseModel):
    user_results: UserResults
