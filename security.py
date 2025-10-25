import hashlib
import base64
import os

def insecure_hash(password):
    # Intentional Bandit issue: MD5 used
    return hashlib.md5(password.encode()).hexdigest()

def generate_token(user_id):
    data = f"{user_id}:{os.urandom(8)}"
    return base64.b64encode(data.encode()).decode()

def verify_token(token):
    try:
        decoded = base64.b64decode(token.encode()).decode()
        user_id, _ = decoded.split(":")
        return user_id
    except Exception as e:
        print("Token verification failed:", e)
        return None
