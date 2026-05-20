import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(f"status_code: {response.status_code}")

if response.status_code == 200:
    data = response.json()

    print(f"Post ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")