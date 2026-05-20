import requests

new_post = {
    "title" : "Learning REST API",
    "body" : "Post request example",
    "userID" : 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json = new_post
)

print(f"Status code: {response.status_code}")

if response.status_code == 201:
    print("created successfully")
    print(response.json())
    data = response.json()
    print(data['id'])
    print(data['title'])
    print(data['body'])

