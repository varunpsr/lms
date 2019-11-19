from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Librarian, Library
from .serializers import UserRegistrationSerializer


@api_view(['POST', ])
def create_user(request):
    """
    Create user view
    """
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def logout(request):
    if request.method == 'GET':
        try:
            request.user.auth_token.delete()
        except (AttributeError, Exception):
            pass
        return Response(status=status.HTTP_200_OK)
