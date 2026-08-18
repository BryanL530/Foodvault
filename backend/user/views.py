from rest_framework import views, response, exceptions, permissions
from user.serializers import UserSerializers
from user import services as user_services
from user import authentication as user_auth


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Data Processing
        data = serializer.validated_data
        serializer.instance = user_services.create_user(user_data=data) # pyright: ignore[reportArgumentType]
        
        return response.Response(data=serializer.data)
    
class LoginAPI(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        # Find user account and check credentials
        user = user_services.user_email_selector(email=email)
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        
        token = user_services.create_token(user_id=user.id) # type: ignore
        
        resp = response.Response()
        resp.set_cookie(key='jwt', value=token, httponly=True)
        return resp
    
class UserAPI(views.APIView):
    """
    This enpoint can only be used when the user is authenticated
    """
    authentication_classes = [user_auth.CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializers(user)
        return response.Response(serializer.data)
    
class LogoutAPI(views.APIView):
    authentication_classes = [user_auth.CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        resp = response.Response()
        resp.delete_cookie(key='jwt')
        resp.data = {'message': 'User session cookie removed'}
        return resp
    
        