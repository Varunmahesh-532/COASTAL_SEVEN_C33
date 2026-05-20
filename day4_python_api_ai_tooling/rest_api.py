import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1.Get request
response = requests.get(f"{BASE_URL}/users/1")

if response.status_code == 200:
    user_data = response.json()
    print(f"User Found: {user_data['name']} working at {user_data['company']['name']}")
else:
    print(f"Failed to retrieve user data. Status code: {response.status_code}")

# 2. Post request
new_post = {
    "title": "My Mentor Session",
    "body": "Learning APIs from scratch!",
    "userId": 1
}

post_response = requests.post(f"{BASE_URL}/posts", json = new_post)
print(f"Creation Status Code: {post_response.status_code}")

