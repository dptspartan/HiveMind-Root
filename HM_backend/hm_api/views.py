from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import FriendRequest, Friends
from django.db.models import Q
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
                                 'user': user.id})
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
                                 'User': user.id})
            else:
                return Response({'message': 'User already exists'}, status=401)
    @api_view(['POST'])
    def findUser(request):
        if (request.method == 'POST'):
            search_text = request.POST.get("searchText")
            me = request.POST.get("user")
            matching_users = User.objects.filter(
            Q(username__icontains=search_text) |  # Case-insensitive search in username
            Q(first_name__icontains=search_text) |  # Search in first name
            Q(last_name__icontains=search_text)  # Search in last name
        )
            if matching_users.exists():
                serialized_users = []
                for user in matching_users:
                    frndStatus = 'Add Friend'
                    if FriendRequest.objects.filter(from_user=me, to_user=user.id).exists() or FriendRequest.objects.filter(from_user=user.id, to_user=me).exists():
                        frndStatus = 'Request Sent'
                    serialized_user = {
                        'id': user.id,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'friend_status': frndStatus,
                        # Add other fields as needed
                    }
                    serialized_users.append(serialized_user)
                return Response({'message': "User Found",
                                 'Users': serialized_users})
            else:
                return Response({'message': 'User Not Found'}, status=401)

class FriendsView:
    @api_view(['POST'])
    def send_friend_request(request):
        """Creates a friend request from from_user to to_user."""
            #print(request.body)
            # Assuming a JSON request
        from_user = request.POST.get("from_user")
        to_user = request.POST.get("to_user")
        from_user = User.objects.get(id = int(from_user))
        to_user = User.objects.get(id = int(to_user))
            # Check for existing request or friendship
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists() or FriendRequest.objects.filter(from_user=to_user, to_user=from_user).exists():
                return Response({'message': 'Friend Request already exists'}, status=401)  # Request already exists
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return Response({'message': 'Friend Request Sent'})