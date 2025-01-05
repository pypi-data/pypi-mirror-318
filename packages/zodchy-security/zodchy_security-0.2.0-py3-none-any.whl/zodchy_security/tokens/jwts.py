import typing

import jwt
import datetime

T = typing.TypeVar("T")


class JWTTokenProducer(typing.Generic[T]):
    def __init__(
        self,
        secret: str,
        algorithm: str,
        issuer: str
    ):
        self._secret = secret
        self._algorithm = algorithm
        self._issuer = issuer

    def access_token(self, user_id: T, lifetime_in_seconds: int = 300):
        return jwt.encode(
            {
                'user_id': str(user_id),
                'iss': self._secret,
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=lifetime_in_seconds)
            },
            self._secret,
            self._algorithm
        )

    def refresh_token(self):
        return jwt.encode(
            {
                'iss': self._secret,
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            },
            self._secret,
            self._algorithm
        )
