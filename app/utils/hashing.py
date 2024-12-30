from hashlib import sha256


def hash_password(password: str) -> str:
    """Hash the password using SHA256."""
    return sha256(password.encode()).hexdigest()
