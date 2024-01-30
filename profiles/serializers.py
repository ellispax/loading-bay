from rest_framework import serializers
from .models import GeneralUserProflie

class GeneralUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralUserProflie
        fields = '__all__'

# class CompanyUserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CompanyUserProfile
#         fields = '__all__'