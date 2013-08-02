from rest_framework import serializers
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    
    nickname = serializers.CharField()
    birthday = serializers.DateField()

    class Meta:
        model = UserProfile
