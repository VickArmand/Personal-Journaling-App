from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser
from django.contrib.auth import login, logout, get_user
from django.contrib.auth.models import AnonymousUser
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signin(request):
    """"""
    if not request.data.get('email'):
        return JsonResponse({"error": "Email required"}, status=status.HTTP_401_UNAUTHORIZED)
    elif not request.data.get('password'):
        return JsonResponse({"error": "Password required"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        user = CustomUser.objects.get(email=request.data.get('email'))
        if user.check_password(request.data.get('password')):
            login(request=request, user=user)
            return JsonResponse({"Success": 'Logged in'}, status=status.HTTP_202_ACCEPTED) 
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User Doesn't Exist"}, status=status.HTTP_404_NOT_FOUND)


   
@api_view(['POST'])
def register(request):
    """"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        return JsonResponse({"success": "User Registered"}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user(request):
    """"""
    user = get_user(request)
    if isinstance(user, AnonymousUser):
        return JsonResponse({"error": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user, data=request.data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    if request.data.get('password'):
        user.set_password(request.data['password'])
        user.save()
    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def signout(request):
    """"""
    logout(request)
    return JsonResponse({"success": "Logged out"}, status=status.HTTP_202_ACCEPTED)
