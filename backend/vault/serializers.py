from rest_framework import serializers
from vault.models import Vault, VaultMember

class VaultSerializers(serializers.Serializer):   
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    
    
    
class MemberSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    vault_id = serializers.IntegerField(read_only=True)
    memeber_id = serializers.IntegerField(read_only=True)
    role = serializers.CharField()