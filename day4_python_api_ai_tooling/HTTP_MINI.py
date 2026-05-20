import requests

while True:

    print("\n===== HTTP STATUS CODE MINI PROJECT =====")
    print("\n1. GET Existing Post")
    print("2. GET Invalid Post")
    print("3. CREATE New Post")

    choice = input("Enter your choice (1, 2, or 3):")

    if choice == '1':
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            print("SUCCESS: Data fetched successfully")
            data = response.json()

    elif choice == '2':
        response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
        print(f"Status code:{response.status_code}")
        if response.status_code == 404:
            print("ERROR: Post not found")
        else:
            print("Unexpected status code:", response.status_code)

    elif choice == '3':
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
            print("Post created successfully")
            data = response.json()
            print("New Post ID:", data['id'])
            print("Title:", data['title'])
        
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")



