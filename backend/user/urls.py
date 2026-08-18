from django.urls import path
from user import views as user_views

urlpatterns = [
   path('register/', user_views.RegisterAPI.as_view(), name='Register'),
   path('login/', user_views.LoginAPI.as_view(), name='Login'),
   path('check_login/', user_views.UserAPI.as_view(), name='Login Status'),
   path('logout/', user_views.LogoutAPI.as_view(), name='Logout'),
]


