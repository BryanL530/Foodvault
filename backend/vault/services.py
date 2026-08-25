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

def get_vault_list(user: 'User') -> 'QuerySet[Vault]':
    return user.vaults.all()  # pyright: ignore[reportAttributeAccessIssue]

def create_member(vault, member, role):
    return VaultMember.objects.create(
        vault_id=vault,
        member_id=member,
        role=role
    )