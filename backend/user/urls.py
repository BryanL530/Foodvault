from django.urls import path
from . import views as user_views

urlpatterns = [
   path('register/', user_views.RegisterAPI.as_view(), name='Register')
]


