from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from profiles.models import GeneralUserProflie
from profiles.serializers import GeneralUserProfileSerializer


# Create your views here.
User = get_user_model()

@api_view(['POST'])
def register(request):                  #register a general user (job applicant)
    userData = {
        'email': request.data.get('email'),
        'username': request.data.get('username'),
        'password': request.data.get('password')
    }
    profiledata = {
        'firstName': request.data.get('firstName'),
        'lastName': request.data.get('lastName'),
        'gender': request.data.get('gender'),
        'address': request.data.get('address'),
        'phoneNumber': request.data.get('phoneNumber'),
        'profile_image': request.data.get('profile_image')
    }

    user_serializer = UserSerializer(data=userData)
    general_profile_serializer = GeneralUserProfileSerializer(data=profiledata)

    if user_serializer.is_valid():              #user serializer used to create the Auth User account for login
        print(user_serializer)
        user = user_serializer.save()

        # Update profiledata with user ID
        profiledata['user'] = user.id
        general_profile_serializer = GeneralUserProfileSerializer(data=profiledata)
        print(general_profile_serializer)

        try:
            general_profile_serializer.is_valid(raise_exception=True)
            general_profile_serializer.save()   #profile serializer for creating their profile after their auth account has been created
        except serializers.ValidationError as e:
            # Rollback user creation
            user.delete()
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_superuser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = User.objects.create_superuser(email=email, username=username, password=password)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)