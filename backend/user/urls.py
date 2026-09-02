from django.urls import path
from user import views as user_views

urlpatterns = [
    path('user/', user_views.UserApi.as_view(), name='User Api'),
    path('login/', user_views.LoginApi.as_view(), name='Login Api'),
    path('logout/', user_views.LogoutApi.as_view(), name='Logout Api'),
    path('user/me/', user_views.MeApi.as_view(), name='Me API'),
]


