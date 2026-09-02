from django.db.models import QuerySet
from vault.models import Vault, VaultMember
from user.models import User

def create_vault(user: 'User', validated_data):
    instance = Vault.objects.create(**validated_data)   
    create_member(
        vault=instance,
        member=user,
        role=VaultMember.Role.OWNER
    )
    return instance

def create_member(vault, member, role):
    return VaultMember.objects.create(
        vault=vault,
        member=member,
        role=role
    )