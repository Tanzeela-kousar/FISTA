import hashlib
import base64
import os
import logging

logger = logging.getLogger(__name__)

def insecure_hash(password: str) -> str:
    # Intentional Bandit issue: MD5 used
    return hashlib.md5(password.encode()).hexdigest()


def generate_token(user_id: str) -> str:
    data = f'{user_id}:{os.urandom(8)}'
    return base64.b64encode(data.encode()).decode()


def verify_token(token: str) -> str | None:
    try:
        decoded = base64.b64decode(token.encode()).decode()
        user_id, _ = decoded.split(":")
        return user_id
    except base64.binascii.Error as e:
        logger.error("Token verification failed: %s", e)
        return None
    except Exception as e:
        logger.exception("An unexpected error occurred during token verification: %s", e)
        return None
