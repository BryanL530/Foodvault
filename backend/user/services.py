import datetime
import jwt
from dataclasses import dataclass
from typing import Optional
from django.conf import settings
from user.models import User

@dataclass(frozen=True)
class UserDTO:
    user_name: str
    first_name: str
    last_name: str
    email: str
    password: Optional[str] = None
    
    @classmethod
    def from_instance(cls, user: 'User') -> 'UserDTO':
        return cls(
            user_name=user.user_name,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )


def create_user(user_data: 'UserDTO') -> 'UserDTO':
    instance = User(
        user_name=user_data.user_name,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
    )
    
    if user_data.password is None:
        raise ValueError('User must contain a password')
    
    instance.set_password(user_data.password)
    instance.full_clean()
    instance.save()
    return UserDTO.from_instance(instance)


def authenticate_user(user_name: str, password: str) -> Optional['User']:
    user = User.objects.filter(user_name=user_name).first()
    if user is None:
        return None
    if not user.check_password(password):
        return None
    return user


def create_token(user_name: str) -> str:
    payload = {
        'user_name': user_name,
        'iat': datetime.datetime.now(datetime.timezone.utc),
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')



