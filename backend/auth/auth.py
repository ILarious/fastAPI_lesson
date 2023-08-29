from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from config import SECRET_KEY

cookie_transports = CookieTransport(cookie_max_age=3600)

SECRET = SECRET_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transports,
    get_strategy=get_jwt_strategy
)
