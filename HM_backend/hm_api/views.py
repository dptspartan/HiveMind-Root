from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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
            return Response({'message': 'Login Successful'})
        else:
            return Response({'message': 'Login Failed'}, status=401)
def logout_user(request):
    logout(request)
    return Response({'message': 'Logout Successful'})
@csrf_exempt
@api_view(['POST'])
def register_user(request):
    if(request.method == 'POST'):
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            return Response({'message': 'User Created'})
        else:
            return Response({'message': 'User already exists'}, status=401)
