from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserExperience, UserProject, UserSkill, UserCertificate, UserLink


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fname', 'lname', 'isDiscoverable', 'profilePicture' , 'position', 'biography', 'qualification', 'experience', 'location', 'createdAt']
        # fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExperience
        fields = '__all__'


class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = '__all__'


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = '__all__'


class UserCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = '__all__'


class UserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLink
        fields = '__all__'
