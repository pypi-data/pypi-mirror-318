import secrets

def generate_uuid() -> str:
    """Generate a secure, random, and unique ID."""
    return f"{secrets.token_hex(16)}"  # 32-character hexadecimal string
