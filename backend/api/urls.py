from django.contrib import admin
from django.urls import path, include
import user.urls as user_urls
import vault.urls as vault_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_urls)),
    path('', include(vault_urls)),
]
