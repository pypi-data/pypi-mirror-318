import requests
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class User:
    user_id: str
    email: str
    name: str
    avatar: Optional[str]
    user_type: str
    org_id: str
    role_id: str
    team_id: Optional[str]
    timezone: Optional[str]

@dataclass
class SuperleapResponse:
    success: bool
    data: List[User]

class SuperleapClient:
    BASE_URL = "https://dev-app.superleap.com/api/v1"
    
    def __init__(self, token: str):
        """Initialize the Superleap client with an authentication token.
        
        Args:
            token (str): Bearer token for authentication
        """
        self.token = token
    
    def poll(self) -> SuperleapResponse:
        """Fetch user list from the API.
        
        Returns:
            SuperleapResponse: Object containing success status and list of User objects
        
        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        
        response = requests.post(
            f"{self.BASE_URL}/org/user/list",
            headers=headers
        )
        response.raise_for_status()
        raw_data = response.json()
        
        users = [User(**user_data) for user_data in raw_data["data"]]
        
        return SuperleapResponse(
            success=raw_data["success"],
            data=users
        )