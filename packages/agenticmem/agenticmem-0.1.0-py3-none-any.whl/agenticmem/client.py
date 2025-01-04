from typing import List, Optional
from datetime import datetime
import requests
from urllib.parse import urljoin

from server.api_schema.service_schemas import (
    Interaction,
    InteractionRequest,
    UserProfile,
    PublishUserInteractionRequest,
    PublishUserInteractionResponse,
    DeleteUserProfileRequest,
    DeleteUserProfileResponse,
    DeleteUserInteractionRequest,
    DeleteUserInteractionResponse,
)
from server.api_schema.login_schema import Token


class AgenticMemClient:
    """Client for interacting with the AgenticMem API."""

    def __init__(self, api_key: str):
        """Initialize the AgenticMem client.

        Args:
            api_key (str): Your API key for authentication
        """
        self.api_key = api_key
        self.base_url = "https://api.agenticmem.com"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def _make_request(self, method: str, endpoint: str, **kwargs):
        """Make an HTTP request to the API.

        Args:
            method (str): HTTP method (GET, POST, DELETE)
            endpoint (str): API endpoint
            **kwargs: Additional arguments to pass to requests

        Returns:
            dict: API response
        """
        url = urljoin(self.base_url, endpoint)
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    def login(self, email: str, password: str) -> Token:
        """Login to the AgenticMem API.

        Args:
            email (str): The user's email
            password (str): The user's password

        Returns:
            Token: Response containing success status and message
        """
        response = self._make_request("POST", "/api/login", json={"email": email, "password": password})
        return Token(**response)

    def publish_interaction(
        self,
        user_id: str,
        request_id: str,
        interaction_requests: List[InteractionRequest]
    ) -> PublishUserInteractionResponse:
        """Publish user interactions.

        Args:
            user_id (str): The user ID
            request_id (str): The request ID
            interaction_requests (List[InteractionRequest]): List of interaction requests

        Returns:
            PublishUserInteractionResponse: Response containing success status and message
        """
        request = PublishUserInteractionRequest(
            user_id=user_id,
            request_id=request_id,
            interaction_requests=interaction_requests
        )
        response = self._make_request("POST", "/api/interactions", json=request.model_dump())
        return PublishUserInteractionResponse(**response)

    def search_interactions(
        self,
        user_id: str,
        request_id: Optional[str] = None,
        query: Optional[str] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        most_recent_k: Optional[int] = None
    ) -> List[Interaction]:
        """Search for user interactions.

        Args:
            user_id (str): The user ID
            request_id (Optional[str], optional): Filter by request ID
            query (Optional[str], optional): Search query
            start_time (Optional[datetime], optional): Start time filter
            end_time (Optional[datetime], optional): End time filter
            most_recent_k (Optional[int], optional): Limit to most recent K results

        Returns:
            List[Interaction]: List of matching interactions
        """
        params = {
            "user_id": user_id,
            "request_id": request_id,
            "query": query,
            "start_time": start_time,
            "end_time": end_time,
            "most_recent_k": most_recent_k
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        response = self._make_request("GET", "/api/interactions/search", params=params)
        return [Interaction(**interaction) for interaction in response.get("interactions", [])]

    def search_profiles(
        self,
        user_id: str,
        genered_from_request_id: Optional[str] = None,
        query: Optional[str] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        top_k: Optional[int] = None
    ) -> List[UserProfile]:
        """Search for user profiles.

        Args:
            user_id (str): The user ID
            genered_from_request_id (Optional[str], optional): Filter by request ID that generated the profile
            query (Optional[str], optional): Search query
            start_time (Optional[datetime], optional): Start time filter
            end_time (Optional[datetime], optional): End time filter
            top_k (Optional[int], optional): Limit to top K results

        Returns:
            List[UserProfile]: List of matching profiles
        """
        params = {
            "user_id": user_id,
            "genered_from_request_id": genered_from_request_id,
            "query": query,
            "start_time": start_time,
            "end_time": end_time,
            "top_k": top_k
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        response = self._make_request("GET", "/api/profiles/search", params=params)
        return [UserProfile(**profile) for profile in response.get("user_profiles", [])]

    def delete_profile(
        self,
        user_id: str,
        profile_id: str = "",
        profile_search_query: str = ""
    ) -> DeleteUserProfileResponse:
        """Delete user profiles.

        Args:
            user_id (str): The user ID
            profile_id (str, optional): Specific profile ID to delete
            profile_search_query (str, optional): Query to match profiles for deletion

        Returns:
            DeleteUserProfileResponse: Response containing success status and message
        """
        request = DeleteUserProfileRequest(
            user_id=user_id,
            profile_id=profile_id,
            profile_search_query=profile_search_query
        )
        response = self._make_request("DELETE", "/api/profiles", json=request.model_dump())
        return DeleteUserProfileResponse(**response)

    def delete_interaction(
        self,
        user_id: str,
        interaction_id: str
    ) -> DeleteUserInteractionResponse:
        """Delete a user interaction.

        Args:
            user_id (str): The user ID
            interaction_id (str): The interaction ID to delete

        Returns:
            DeleteUserInteractionResponse: Response containing success status and message
        """
        request = DeleteUserInteractionRequest(
            user_id=user_id,
            interaction_id=interaction_id
        )
        response = self._make_request("DELETE", "/api/interactions", json=request.model_dump())
        return DeleteUserInteractionResponse(**response) 