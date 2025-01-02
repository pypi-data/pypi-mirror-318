import json
from typing import Any, Dict, List, Optional, Self, Union

import httpx

from xclient.models.actions import FavoriteResult, RetweetResult
from xclient.models.error import Error, ErrorResponse
from xclient.models.timeline import Timeline
from xclient.models.tweet import (
    CreateTweetMedia,
    CreateTweetVariables,
    DeleteTweetResult,
    ItemResult,
    MediaEntity,
)
from xclient.models.user import UserResults


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/58.0.3029.110 Safari/537.36"
)

BASE_URL = "https://x.com/i/api/graphql"

BLUE_VERIFIED_FOLLOWERS_OPERATION = "UdtZY8FOW3ULVnjDU52BVg/BlueVerifiedFollowers"
FOLLOWERS_OPERATION = "gwv4MK0diCpAJ79u7op1Lg/Followers"
FOLLOWING_OPERATION = "eWTmcJY3EMh-dxIR7CYTKw/Following"
FAVORITE_TWEET_OPERATION = "lI07N6Otwv1PhnEgXILM7A/FavoriteTweet"
UNFAVORITE_TWEET_OPERATION = "ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet"
CREATE_RETWEET_OPERATION = "ojPdsZsimiJrUGLR1sjUtA/CreateRetweet"
DELETE_RETWEET_OPERATION = "iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet"
USER_BY_SCREEN_NAME_OPERATION = "laYnJPCAcVo0o6pzcnlVxQ/UserByScreenName"
USERS_BY_REST_IDS_OPERATION = "lc85bOG5T3IIS4u485VtBg/UsersByRestIds"
USER_TWEETS_OPERATION = "Tg82Ez_kxVaJf7OPbUdbCg/UserTweets"
HOME_LATEST_TIMELINE_OPERATION = "HyuV8ml52TYmyUjyrDq1CQ/HomeLatestTimeline"
CREATE_TWEET_OPERATION = "znq7jUAqRjmPj7IszLem5Q/CreateTweet"
DELETE_TWEET_OPERATION = "VaenaVgh5q5ih7kvyVjgtg/DeleteTweet"


class XError(Exception):
    def __init__(self, error: Error):
        self.error = error
        super().__init__(f"X API Error: {error.message}")


class XClient:
    def __init__(
        self,
        auth_token: str,
        api_token: str,
        csrf_token: str,
        client_transaction_id: str,
        *,
        user_agent: Optional[str] = None,
        timeout: float = 30.0,
        client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        """Initialize the X API client.

        Args:
            auth_token: X authentication token
            api_token: X API token
            csrf_token: CSRF token
            client_transaction_id: Client transaction ID
            user_agent: Custom user agent string (optional)
            timeout: Request timeout in seconds (default: 30.0)
            client: Custom httpx.AsyncClient instance (optional)
        """
        self.auth_token = auth_token
        self.api_token = api_token
        self.csrf_token = csrf_token
        self.client_transaction_id = client_transaction_id
        self.user_agent = user_agent or DEFAULT_USER_AGENT
        self._client = client or httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._client.aclose()

    @property
    def headers(self) -> Dict[str, str]:
        """Get the default headers for API requests."""
        return {
            "User-Agent": self.user_agent,
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "X-CSRF-Token": self.csrf_token,
            "X-Client-Transaction-Id": self.client_transaction_id,
        }

    @property
    def cookies(self) -> Dict[str, str]:
        """Get the default cookies for API requests."""
        return {
            "auth_token": self.auth_token,
            "ct0": self.csrf_token,
        }

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """Handle the API response and raise appropriate exceptions."""
        if response.status_code != httpx.codes.OK:
            try:
                error_data = response.json()
                error_response = ErrorResponse.model_validate(error_data)
                if error_response.errors:
                    raise XError(error_response.errors[0])
            except json.JSONDecodeError:
                response.raise_for_status()
            except ValueError as e:
                raise ValueError(f"Invalid error response format: {str(e)}") from e

        return response.json()

    async def _get(
        self,
        operation: str,
        variables: Optional[Dict[str, Any]] = None,
        features: Optional[Dict[str, Any]] = None,
        field_toggles: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a GET request to the X API.

        Args:
            operation: GraphQL operation name
            variables: GraphQL variables
            features: Feature flags
            field_toggles: Field toggles

        Returns:
            API response as a dictionary

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        params = {}

        if variables:
            params["variables"] = json.dumps(variables)
        if features:
            params["features"] = json.dumps(features)
        if field_toggles:
            params["fieldToggles"] = json.dumps(field_toggles)

        response = await self._client.get(
            f"{BASE_URL}/{operation}",
            params=params,
            headers=self.headers,
            cookies=self.cookies,
        )
        return self._handle_response(response)

    async def _post(
        self,
        operation: str,
        variables: Optional[Dict[str, Any]] = None,
        features: Optional[Dict[str, Any]] = None,
        field_toggles: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request to the X API.

        Args:
            operation: GraphQL operation name
            variables: GraphQL variables
            features: Feature flags
            field_toggles: Field toggles

        Returns:
            API response as a dictionary

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        data = {
            "variables": variables or {},
            "features": features or {},
        }

        if field_toggles:
            data["fieldToggles"] = field_toggles

        response = await self._client.post(
            f"{BASE_URL}/{operation}",
            json=data,
            headers=self.headers,
            cookies=self.cookies,
        )
        return self._handle_response(response)

    async def get_blue_verified_followers(
        self,
        user_id: str,
        count: int = 20,
        include_promoted_content: bool = False,
    ) -> Timeline:
        """Get a user's blue verified followers.

        Args:
            user_id: User ID
            count: Number of verified followers to fetch (default: 20)
            include_promoted_content: Include promoted content (default: False)

        Returns:
            Timeline: Pydantic model containing the blue verified followers timeline data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "userId": user_id,
            "count": count,
            "includePromotedContent": include_promoted_content,
        }
        features = {
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "articles_preview_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "rweb_video_timestamps_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }

        response = await self._get(BLUE_VERIFIED_FOLLOWERS_OPERATION, variables, features)
        timeline_data = response["data"]["user"]["result"]["timeline"]["timeline"]
        return Timeline.model_validate(timeline_data)

    async def get_followers(
        self,
        user_id: str,
        count: int = 20,
        include_promoted_content: bool = False,
    ) -> Timeline:
        """Get a user's followers.

        Args:
            user_id: User ID
            count: Number of followers to fetch (default: 20)
            include_promoted_content: Include promoted content (default: False)

        Returns:
            Timeline: Pydantic model containing the followers timeline data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "userId": user_id,
            "count": count,
            "includePromotedContent": include_promoted_content,
        }
        features = {
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "articles_preview_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "rweb_video_timestamps_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }

        response = await self._get(FOLLOWERS_OPERATION, variables, features)
        timeline_data = response["data"]["user"]["result"]["timeline"]["timeline"]
        return Timeline.model_validate(timeline_data)

    async def get_following(
        self,
        user_id: str,
        count: int = 20,
        include_promoted_content: bool = False,
    ) -> Timeline:
        """Get a list of users that the specified user follows.

        Args:
            user_id: User ID
            count: Number of following users to fetch (default: 20)
            include_promoted_content: Include promoted content (default: False)

        Returns:
            Timeline: Pydantic model containing the following timeline data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "userId": user_id,
            "count": count,
            "includePromotedContent": include_promoted_content,
        }
        features = {
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "articles_preview_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "rweb_video_timestamps_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }

        response = await self._get(FOLLOWING_OPERATION, variables, features)
        timeline_data = response["data"]["user"]["result"]["timeline"]["timeline"]
        return Timeline.model_validate(timeline_data)

    async def get_users_by_rest_ids(
        self,
        user_ids: List[str],
        include_tipjar: bool = True,
        exclude_directive: bool = True,
        verified_phone_label: bool = False,
        skip_profile_image_extensions: bool = False,
        timeline_navigation: bool = True,
    ) -> List["UserResults"]:
        """Get multiple users by their rest IDs.

        Args:
            user_ids: List of user IDs to fetch
            include_tipjar: Include tip jar information
            exclude_directive: Enable GraphQL exclude directive
            verified_phone_label: Enable verified phone label
            skip_profile_image_extensions: Skip profile image extensions
            timeline_navigation: Enable timeline navigation

        Returns:
            List[UserResults]: List of Pydantic models containing user data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "userIds": user_ids,
        }
        features = {
            "rweb_tipjar_consumption_enabled": include_tipjar,
            "responsive_web_graphql_exclude_directive_enabled": exclude_directive,
            "verified_phone_label_enabled": verified_phone_label,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": skip_profile_image_extensions,
            "responsive_web_graphql_timeline_navigation_enabled": timeline_navigation,
        }

        response = await self._get(USERS_BY_REST_IDS_OPERATION, variables, features)
        return [UserResults.model_validate(user) for user in response["data"]["users"]]

    async def get_user_by_screenname(self, screenname: str) -> UserResults:
        """Get a user by their screen name.

        Args:
            screenname: User screen name

        Returns:
            UserResults: Pydantic model containing the user data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {"screen_name": screenname}
        features = {
            "highlights_tweets_tab_ui_enabled": True,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "hidden_profile_subscriptions_enabled": True,
            "subscriptions_verification_info_verified_since_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "responsive_web_twitter_article_notes_tab_enabled": True,
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "subscriptions_verification_info_is_identity_verified_enabled": True,
            "verified_phone_label_enabled": False,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "subscriptions_feature_can_gift_premium": True,
        }
        field_toggles = {"withAuxiliaryUserLabels": False}

        response = await self._get(USER_BY_SCREEN_NAME_OPERATION, variables, features, field_toggles)
        return UserResults.model_validate(response["data"]["user"])

    async def get_user_tweets(
        self,
        user_id: str,
        count: int = 20,
        include_promoted_content: bool = False,
        with_quick_promote_eligibility_tweet_fields: bool = True,
        with_voice: bool = True,
        withV2Timeline: bool = True,
    ) -> Timeline:
        """Get a user's tweets.

        Args:
            user_id: User ID
            count: Number of tweets to fetch (default: 20)
            include_promoted_content: Include promoted content (default: False)
            with_quick_promote_eligibility_tweet_fields: Include quick promote eligibility tweet fields (default: False)
            with_voice: Include voice (default: False)
            withV2Timeline: Include V2 timeline (default: False)

        Returns:
            Timeline: Pydantic model containing the timeline data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "userId": user_id,
            "count": count,
            "includePromotedContent": include_promoted_content,
            "withQuickPromoteEligibilityTweetFields": with_quick_promote_eligibility_tweet_fields,
            "withVoice": with_voice,
            "withV2Timeline": withV2Timeline,
        }
        features = {
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "articles_preview_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "rweb_video_timestamps_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }
        field_toggles = {"withArticlePlainText": False}

        response = await self._get(
            USER_TWEETS_OPERATION,
            variables,
            features,
            field_toggles,
        )
        timeline_data = response["data"]["user"]["result"]["timeline_v2"]["timeline"]
        return Timeline.model_validate(timeline_data)

    async def get_home_timeline(
        self,
        count: int = 40,
        cursor: Optional[str] = None,
        include_promoted_content: bool = False,
        latest_control_available: bool = True,
        seen_tweet_ids: Optional[List[str]] = None,
    ) -> Timeline:
        """Get the home timeline.

        Args:
            count: Number of tweets to fetch (default: 40)
            cursor: Cursor for pagination
            include_promoted_content: Include promoted content (default: True)
            latest_control_available: Whether latest control is available (default: True)
            seen_tweet_ids: List of tweet IDs that have been seen

        Returns:
            Timeline: Pydantic model containing the timeline data

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables: Dict[str, Any] = {
            "count": count,
            "includePromotedContent": include_promoted_content,
            "latestControlAvailable": latest_control_available,
        }
        if cursor:
            variables["cursor"] = cursor

        if seen_tweet_ids:
            variables["seenTweetIds"] = seen_tweet_ids

        features = {
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "articles_preview_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "rweb_video_timestamps_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }

        response = await self._post(HOME_LATEST_TIMELINE_OPERATION, variables=variables, features=features)
        return Timeline.model_validate(response["data"]["home"]["home_timeline_urt"])

    async def favorite_tweet(self, tweet_id: str) -> FavoriteResult:
        """Like/favorite a tweet.

        Args:
            tweet_id: ID of the tweet to favorite

        Returns:
            FavoriteResponse: Response from the API containing confirmation

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {"tweet_id": tweet_id}

        response = await self._post(FAVORITE_TWEET_OPERATION, variables=variables)
        return FavoriteResult.model_validate(response["data"])

    async def unfavorite_tweet(self, tweet_id: str) -> FavoriteResult:
        """Unlike/unfavorite a tweet.

        Args:
            tweet_id: ID of the tweet to unfavorite

        Returns:
            FavoriteResponse: Response from the API containing confirmation

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {"tweet_id": tweet_id}

        response = await self._post(UNFAVORITE_TWEET_OPERATION, variables=variables)
        return FavoriteResult.model_validate(response["data"])

    async def create_retweet(self, tweet_id: str, dark_request: bool = False) -> RetweetResult:
        """Retweet a tweet.

        Args:
            tweet_id: ID of the tweet to retweet
            dark_request: Whether this is a dark request (default: False)

        Returns:
            Tweet: The created retweet

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {"tweet_id": tweet_id, "dark_request": dark_request}

        response = await self._post(CREATE_RETWEET_OPERATION, variables=variables)
        result = response["data"]["create_retweet"]["retweet_results"]["result"]
        return RetweetResult(rest_id=result["rest_id"], full_text=result["legacy"]["full_text"])

    async def delete_retweet(self, tweet_id: str, dark_request: bool = False) -> RetweetResult:
        """Remove a retweet.

        Args:
           tweet_id: ID of the source tweet to unretweet
            dark_request: Whether this is a dark request (default: False)

        Returns:
            Tweet: The original source tweet

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "source_tweet_id": tweet_id,
            "dark_request": dark_request,
        }

        response = await self._post(DELETE_RETWEET_OPERATION, variables=variables)
        result = response["data"]["unretweet"]["source_tweet_results"]["result"]
        return RetweetResult(rest_id=result["rest_id"], full_text=result["legacy"]["full_text"])

    async def create_tweet(
        self,
        text: str,
        *,
        media_ids: Optional[List[Union[str, MediaEntity]]] = None,
        possibly_sensitive: bool = False,
        dark_request: bool = False,
        semantic_annotation_ids: Optional[List[str]] = None,
        disallowed_reply_options: Optional[List[str]] = None,
        reply_to_tweet_id: Optional[str] = None,
        quote_tweet_id: Optional[str] = None,
    ) -> ItemResult:
        """Create a new tweet with optional media attachments.

        Args:
            text: The text content of the tweet
            media_ids: Optional list of media IDs or MediaEntity objects to attach to the tweet
            possibly_sensitive: Whether the media is possibly sensitive (default: False)
            dark_request: Whether this is a dark request (default: False)
            semantic_annotation_ids: List of semantic annotation IDs (optional)
            disallowed_reply_options: List of disallowed reply options (optional)
            reply_to_tweet_id: ID of the tweet to reply to (optional)
            quote_tweet_id: ID of the tweet to quote (optional)

        Returns:
            ItemResult: The created tweet result

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        media = None
        if media_ids:
            media_entities = []
            for media_item in media_ids:
                if isinstance(media_item, str):
                    media_entities.append(MediaEntity(media_id=media_item))
                elif isinstance(media_item, MediaEntity):
                    media_entities.append(media_item)
                else:
                    raise ValueError("Media items must be either strings or MediaEntity objects")

            media = CreateTweetMedia(media_entities=media_entities, possibly_sensitive=possibly_sensitive)

        reply = None
        if reply_to_tweet_id:
            reply = {
                "in_reply_to_tweet_id": reply_to_tweet_id,
                "exclude_reply_user_ids": [],
            }

        variables = CreateTweetVariables(
            tweet_text=text,
            dark_request=dark_request,
            media=media,
            semantic_annotation_ids=semantic_annotation_ids or [],
            disallowed_reply_options=disallowed_reply_options,
            reply=reply,
            quote_tweet_id=quote_tweet_id,
        )

        features = {
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "articles_preview_enabled": True,
            "rweb_video_timestamps_enabled": True,
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }

        response = await self._post(
            CREATE_TWEET_OPERATION,
            variables=variables.model_dump(exclude_none=True),
            features=features,
        )
        return ItemResult.model_validate(response["data"]["create_tweet"]["tweet_results"])

    async def delete_tweet(self, tweet_id: str, dark_request: bool = False) -> DeleteTweetResult:
        """Delete a tweet.

        Args:
            tweet_id: ID of the tweet to delete
            dark_request: Whether this is a dark request (default: False)

        Returns:
            DeleteTweetResult: Response confirming the deletion

        Raises:
            XAPIError: If the API returns an error response
            httpx.HTTPError: If there's a network or HTTP-related error
            ValueError: If the error response format is invalid
        """
        variables = {
            "tweet_id": tweet_id,
            "dark_request": dark_request,
        }

        response = await self._post(DELETE_TWEET_OPERATION, variables=variables)
        return DeleteTweetResult.model_validate(response["data"]["delete_tweet"])
