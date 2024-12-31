# Superleap SDK

A Python SDK for interacting with the Superleap API.

## Installation

```bash
pip install superleap-sdk
```

## Usage

```python
from superleap import SuperleapClient

# Initialize the client
client = SuperleapClient("YOUR_TOKEN_HERE")

# Fetch user data
response = client.poll()

# Access the data
print(f"Success: {response.success}")
for user in response.data:
    print(f"User: {user.name} ({user.email})")
```
