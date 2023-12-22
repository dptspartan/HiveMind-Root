from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import FriendRequest, Friends
import json

class UserView:
    @api_view(['GET'])
    def hello_world(request):
        return Response({'message': 'Hello, world!'})


    @api_view(['POST'])
    def login_user(request):
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user =  authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return Response({'message': 'Login Successful',
                                 'User': user})
            else:
                return Response({'message': 'Login Failed'}, status=401)
    def logout_user(request):
        logout(request)
        return Response({'message': 'Logout Successful'})

    @api_view(['POST'])
    def register_user(request):
        if(request.method == 'POST'):
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                return Response({'message': 'User Created',
                                 'User': user})
            else:
                return Response({'message': 'User already exists'}, status=401)

class FriendsView:
    @api_view(['POST'])
    def send_friend_request(request):
        """Creates a friend request from from_user to to_user."""
            #print(request.body)
            # Assuming a JSON request
        from_user = request.POST.get("from_user")
        to_user = request.POST.get("to_user")
            # Check for existing request or friendship
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists() or FriendRequest.objects.filter(from_user=to_user, to_user=from_user).exists():
                return False  # Request already exists
        if Friends.objects.filter(from_user=from_user, to_user=to_user).exists() or Friends.objects.filter(from_user=to_user, to_user=from_user).exists():
                return False  # Already friends
            # Create the friend request
        friend_request = FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return friend_request