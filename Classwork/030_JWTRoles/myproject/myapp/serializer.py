from rest_framework import serializers
from myapp.models import CustomeUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomeUser
        fields='__all__'
        
    def create(self, validated_data):
        user = CustomeUser.objects.create_user(phone=validated_data['phone'],password=validated_data['password'],role=validated_data['role'])
        return user
        