import logging

# Configuring the logging to display DEBUG level and above
logging.basicConfig(level=logging.DEBUG)

def user_login(username):
    # Fixed the string interpolation formatting here
    logging.debug(f"Attempting login sequence for user: {username}")
    
    if username == "admin":
        logging.warning("Admin access granted! High privilege session started.")
        return True
    elif username == "banned_user":
        logging.error(f"Login denied: Account '{username}' is locked.")
        return False
    else:
        logging.info(f"User '{username}' logged in successfully.")
        return True
    
user_login("varun")
user_login("admin")
user_login("banned_user")