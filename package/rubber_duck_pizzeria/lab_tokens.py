"""Lab: a deliberately fake signing secret, as in the BugHunter lab app."""
import jwt

JWT_SECRET = "secret-but-just-long-enough-for-pyjwt-warn-suppress"  # intentional


def make_token(user_id: int) -> str:
    return jwt.encode({"sub": user_id}, JWT_SECRET, algorithm="HS256")
