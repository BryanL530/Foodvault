from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)