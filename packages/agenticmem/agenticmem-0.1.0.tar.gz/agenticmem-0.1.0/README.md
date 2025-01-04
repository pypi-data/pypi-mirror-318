# AgenticMem Python Client

A Python client library for interacting with the AgenticMem API. This client provides easy-to-use interfaces for managing user interactions and profiles.

## Installation

```bash
pip install agenticmem
```

## Quick Start

```python
from agenticmem import AgenticMemClient
from agenticmem import UserActionType, InteractionRequest
from datetime import datetime

# Initialize the client
client = AgenticMemClient(
    api_key="your_api_key",
)

# Publish a user interaction
interaction = InteractionRequest(
    timestamp=datetime.now(),
    text_interaction="User clicked on product X",
    user_action=UserActionType.CLICK,
    user_action_description="Clicked on product details button"
)

response = client.publish_interaction(
    user_id="user123",
    request_id="req456",
    interaction_requests=[interaction]
)
print(f"Published interaction: {response.success} - {response.message}")

# Search user profiles
profiles = client.search_profiles(
    user_id="user123",
    query="recent interactions",
    top_k=5
)
for profile in profiles:
    print(f"Profile {profile.profile_id}: {profile.profile_content}")

# Search interactions
interactions = client.search_interactions(
    user_id="user123",
    start_time=datetime(2024, 1, 1),
    end_time=datetime.now()
)
for interaction in interactions:
    print(f"Interaction {interaction.interaction_id}: {interaction.text_interaction}")
```

## Features

- User interaction management
  - Publish user interactions
  - Delete user interactions
  - Search interactions
- User profile management
  - Search user profiles
  - Delete user profiles

## API Response Types

All API methods return strongly-typed responses:

- `publish_interaction()` returns `PublishUserInteractionResponse`
- `search_interactions()` returns `List[Interaction]`
- `search_profiles()` returns `List[UserProfile]`
- `delete_profile()` returns `DeleteUserProfileResponse`
- `delete_interaction()` returns `DeleteUserInteractionResponse`

## Documentation

For detailed documentation, please visit [docs link].

## License

MIT License 