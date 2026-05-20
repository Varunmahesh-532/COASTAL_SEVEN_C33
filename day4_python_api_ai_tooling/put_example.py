import requests

updated_post = {
    'id' : 1,
    'title' : 'Updated Title',
    'body' : 'This is the updated body of the post.',
    'userId' : 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json = updated_post
)

print("Status code:", response.status_code)
if response.status_code == 200:
    print("post successfully")
    print(response.json())
    data = response.json()
    print(data['id'])
    print(data['title'])
    print(data['body'])   
    print(data['userId']) 
