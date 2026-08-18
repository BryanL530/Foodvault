from rest_framework import serializers
from user import services as user_services

class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def to_internal_value(self, data): # type: ignore
        data = super().to_internal_value(data)
        return user_services.UserDataClass(**data)