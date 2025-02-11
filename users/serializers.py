from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(required=False) 
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    level = serializers.ChoiceField(choices=["beginner", "intermediate", "advanced"])
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """Create and return a new User instance, given the validated data."""
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update and return an existing User instance, given the validated data."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
