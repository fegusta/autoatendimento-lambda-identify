import jwt, os

SECRET = os.getenv("JWT_SECRET", "dev-secret")  # depois trocamos por KMS ou Cognito

def mint_jwt(claims: dict) -> str:
    return jwt.encode(claims, SECRET, algorithm="HS256")
