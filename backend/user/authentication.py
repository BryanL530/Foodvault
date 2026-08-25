from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from user.models import User

LOGIN_TOKEN = 'login_token'

class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get(LOGIN_TOKEN)
        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        except jwt.PyJWTError:
            raise exceptions.AuthenticationFailed('Unauthorized')

        user = User.objects.filter(user_name=payload['user_name']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Unauthorized')

        return (user, None)
