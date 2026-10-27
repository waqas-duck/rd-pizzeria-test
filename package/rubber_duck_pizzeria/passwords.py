"""Password hashing for staff accounts."""
import hashlib


def _md5(password: str) -> str:
    # Intentional weak hash (FLAG path RD_WEAK_HASH)
    return hashlib.md5(password.encode("utf-8")).hexdigest()
