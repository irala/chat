import os

conf: dict = {
    "DATABASE_HOST": os.getenv("DATABASE_HOST", "localhost"),
    "DATABASE_PORT": os.getenv("DATABASE_PORT", "8080"),
    "DATABASE_USER": os.getenv("DATABASE_USER", "root"),
    "DATABASE_PASS": os.getenv("DATABASE_PASS", "example"),
    "REFRESH_TOKEN_DELTA": os.getenv("REFRESH_TOKEN_DELTA", 30),
    "ACCESS_TOKEN_DELTA": int(os.getenv("ACCESS_TOKEN_DELTA", 20)),
    "JWT_PASS": os.getenv("JWT_PASS", "1111"),
}
