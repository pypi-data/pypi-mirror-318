from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from models.user import User
from config.settings import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
settings = Settings()


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[settings.jwt_algorithm]
        )
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401)
    except jwt.JWTError:
        raise HTTPException(status_code=401)

    user = await User.get(user_id)
    if user is None:
        raise HTTPException(status_code=401)

    return user


class AuthService:
    def __init__(self):
        self.settings = Settings()

    async def create_access_token(
            self,
            user_id: str,
            expires_delta: Optional[timedelta] = None
    ) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=1)

        payload = {
            "sub": user_id,
            "exp": expire,
            "type": "access"
        }

        token = jwt.encode(
            payload,
            self.settings.jwt_secret,
            algorithm=self.settings.jwt_algorithm
        )

        return token

    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        from passlib.context import CryptContext
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(plain_password, hashed_password)

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = await User.get_by_email(email)
        if not user:
            return None

        if not await self.verify_password(password, user.password):
            return None

        return user