import dataclasses, datetime, jwt
from typing import Optional
from django.conf import settings
from user.models import User
    
@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    password: Optional[str] = None
    id: Optional[int] = None
    
    
    @classmethod
    def from_instance(cls, user: 'User') -> 'UserDataClass':
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id # type: ignore
        )        

def create_user(user_data: 'UserDataClass') -> 'UserDataClass':
    instance = User(
        first_name = user_data.first_name,
        last_name = user_data.last_name,
        email = user_data.email
    )
    
    if user_data.password is not None:
        instance.set_password(user_data.password)
        
    instance.save()
    
    return UserDataClass.from_instance(instance)

def user_email_selector(email: str) -> 'User | None':
    try:
        return User.objects.get(email=email)
    except:
        return None
    

def create_token(user_id: int) -> str:
    paylaod = dict(
        id=user_id,
        iat=datetime.datetime.now(datetime.timezone.utc),
        exp=datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7),
    )
    
    token = jwt.encode(paylaod, settings.JWT_SECRET, algorithm='HS256')
    return token