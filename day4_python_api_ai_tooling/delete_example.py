"""

import requests

def delete_post(post_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return response.status_code

print(delete_post(1))

"""


import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print("Status code:", response.status_code)
if response.status_code == 200:
    print("Deleted successfully")



