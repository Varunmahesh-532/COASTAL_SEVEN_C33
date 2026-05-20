import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

while True:
    print("\n===== REST API POST MANAGER =====")
    print("1. Get Post")
    print("2. Create Post")
    print("3. Update Post")
    print("4. Delete Post")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Get Request
    if choice == '1':
        post_id = input("Enter post Id to retrive:")
        
        response = requests.get(f"{BASE_URL}/{post_id}")

        if response.status_code == 200:
            data = response.json()
            print(data)
            print("ID:", data["id"])
            print("Title:", data["title"])
            print("Body:", data["body"])

        else:
            print(f"Post is not found")

    # Post Request
    elif choice == '2':
        title = input("Enter post title:")
        body = input("Enter post body:")

        new_post = {
            "title": title,
            "body": body,
            "userId": 1
        }

        response = requests.post(BASE_URL, json = new_post)

        if response.status_code == 201:
            data = response.json()
            print("Post created successfully with ID:", data["id"])
        else:
            print("Failed to create Post")

    # Put Request
    elif choice == '3':
        post_id = input("Enter post Id to update:")

        updated_title = input("Enter updated title:")
        updated_body = input("Enter updated body:")

        updated_post = {
            "id" : post_id,
            "title" : updated_title,
            "body" : updated_body,
            "userId" : 1
        }

        response = requests.put(f"{BASE_URL}/{post_id}", json = updated_post)
        if response.status_code == 200:
            data = response.json()
            print("Post updated successfully", data['id'])
        else:
            print("Failed to update Post")  

    # Delete Request
    elif choice == '4':
        post_id = input("Enter post Id to delete:")
        response = requests.delete(f"{BASE_URL}/{post_id}")
        if response.status_code == 200:
            print("Post deleted successfully")
        else:
            print("Failed to delete Post")

    #Exit
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

