from rest_framework import views, permissions, response, status
from django.core.exceptions import ValidationError
from user.services import UserDTO, create_user, authenticate_user, create_token
from user.serializers import UserSerializer
from user.authentication import CustomUserAuthentication, LOGIN_TOKEN

class UserApi(views.APIView):
    authentication_classes = [CustomUserAuthentication]

    def post(self, request):
        '''
        Creates new user account
        '''
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Creating new user
        resp = response.Response()
        
        try:
            user_dto = UserDTO(**serializer.validated_data)
            serializer.instance = create_user(user_data=user_dto)
            resp.data = serializer.data
        except ValidationError as e:
            # Catching errors for exsisted user name or email from database
            resp.data = e.error_dict
            resp.status_code = status.HTTP_400_BAD_REQUEST
        except Exception as e:
            # Exception for any unknown error
            resp.data = {'message': f'Unknown error: {str(e)}'}
            resp.status_code = status.HTTP_400_BAD_REQUEST
        
        return resp

    def get(self, request):
        if request.user is not None:
            return response.Response(request.user)
        return response.Response('Not yet implemented')
    def put(self, request):
        return response.Response('Not yet implemented')
    def delete(self, reqeust):
        return response.Response('Not yet implemented')
    
class LoginApi(views.APIView):
    def post(self, request):
        data = request.data
        user_name = data.get('user_name')
        password = data.get('password')

        if not user_name or not password:
            return response.Response(
                {'message': 'user_name and password are required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate_user(user_name, password)
        if user is None:
            return response.Response(
                {'message': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token = create_token(user.user_name)
        resp = response.Response({'message': f'Logged in as {user}'})
        resp.set_cookie(LOGIN_TOKEN, token, httponly=True, max_age=30 * 24 * 60 * 60)
        return resp
    
class LogoutApi(views.APIView):
    def post(self, request):
        token = request.COOKIES.get(LOGIN_TOKEN)
        if token is None:
            return response.Response({'message': 'User not logged in'}, status=status.HTTP_400_BAD_REQUEST)

        resp = response.Response({'message': 'Logged out'})
        resp.delete_cookie(LOGIN_TOKEN)
        return resp
    
class MeApi(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    def get(self, request):
        token = request.COOKIES.get(LOGIN_TOKEN)
        if token is None:
            return response.Response({'message': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(instance=request.user)
        return response.Response(data=serializer.data)
