from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['name', 'last_name', 'email']

class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

    def validate(self, attrs):

        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError("password missmatch") 
        return attrs

    class Meta:
        model = get_user_model()
        # Tuple of serialized model fields (see link [2])
        fields = ( "email", "name", "last_name", "password", "password2" )