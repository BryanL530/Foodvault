from django.urls import path
from vault import views as vault_views

urlpatterns = [
    path('vault/', vault_views.VaultAPI.as_view(), name='Vault'),
]