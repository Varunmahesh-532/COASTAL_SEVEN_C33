import jwt
import time

SECRET_KEY = "my_super_secret_backend_key_nobody_knows"

def generate_token(user_id, username, role):
    payload = {
        "sub" : user_id,
        "name" : username,
        "role" : role,
        "exp" : time.time() + 600
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return {"success": True, "data": decoded_payload}
    except jwt.ExpiredSignatureError:
        return {"success": False, "error": "Access Denied: Token has expired!"}
    except jwt.InvalidTokenError:
        return {"success": False, "error": "Access Denied: Token signature is tampered or invalid!"}
    

user_token = generate_token(user_id="usr_505", username="alex_dev", role="moderator")
print(f"Generated Token String:\n{user_token}\n")

print("--- Server Verification Processing ---")
result = verify_token(user_token)
print("Result:", result)

tampered_token = user_token + "xyz"
print("\n--- Tampered Token Verification Processing ---")
failed_result = verify_token(tampered_token)
print("Result:", failed_result)
    

    

