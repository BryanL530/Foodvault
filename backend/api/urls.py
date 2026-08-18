from django.contrib import admin
from django.urls import path, include
import user.urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_urls)),
]
