from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import FriendRequest, Friends, Posts, Likes
from .serializers import PostSerializer
from django.db.models import Q

class UserView:
    @api_view(['POST'])
    def login_user(request):
        if(request.method == 'POST'):
            username = request.data["username"]
            password = request.data["password"]
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
            username = request.data["username"]
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            email = request.data["email"]
            password = request.data["password"]
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                return Response({'message': 'User Created',
                                 'User': user.id})
            else:
                return Response({'message': 'User already exists'}, status=401)
    @api_view(['POST'])
    def findUser(request):
        if (request.method == 'POST'):
            search_text = request.data["searchText"]
            if search_text=='':
                return Response({'message': 'Empty Search Value'}, status=401)
            me = request.data["user"]
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
                    elif Friends.objects.filter(from_user=me, to_user=user.id).exists() or Friends.objects.filter(from_user=user.id, to_user=me).exists():
                        frndStatus = 'Friends'
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
        from_user = request.data["from_user"]
        to_user = request.data["to_user"]
        from_user = User.objects.get(id = int(from_user))
        to_user = User.objects.get(id = int(to_user))
            # Check for existing request or friendship
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists() or FriendRequest.objects.filter(from_user=to_user, to_user=from_user).exists():
                return Response({'message': 'Friend Request already exists'}, status=401)  # Request already exists
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return Response({'message': 'Friend Request Sent'})
    @api_view(['POST'])
    def get_friend_requests(request):
        user_id = request.data["user_id"]
        me = User.objects.get(id = int(user_id))
        frnd_reqs = FriendRequest.objects.filter(to_user=me)
        if frnd_reqs.exists() :
            serialized_reqs = []
            for req in frnd_reqs:
                serialized_req = {
                    'id' : req.id,
                    'request_from' : req.from_user.username
                }
                serialized_reqs.append(serialized_req)
            return Response({
                'message': "You have friend phew i was starting to get worried about you",
                'requests':serialized_reqs})
        else:
            return Response({'message': 'No-One wants to be your friend buddy you\'re all alone'}, status=401)
    @api_view(['POST'])
    def accept_friend_request(request):
        frnd_req_id = request.data['request_to_accept']
        print(frnd_req_id)
        frnd_req = FriendRequest.objects.get(pk=frnd_req_id)
        if frnd_req != None:
            Friends.objects.create(from_user=frnd_req.from_user,to_user=frnd_req.to_user)
            frnd_req.delete()
            return Response({'message': 'You are now friends'})
        else:
            return Response({'message': "Cant add you as friends"}, status=401)
    @api_view(['POST'])
    def myFriends(request):
        user_id = request.data['user_id']
        print(user_id)
        user = User.objects.get(pk=user_id)
        friends = Friends.objects.filter(Q(from_user=user) | Q(to_user=user))
        friends = User.objects.filter(id__in=[friend.from_user.id if friend.to_user == user else friend.to_user.id for friend in friends])
        #friends = FriendsView.get_friend_requests(user)
        if friends.exists():
            serialized_friends = []
            for user in friends:
                    serialized_friend = {
                        'id': user.id,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        # Add other fields as needed
                    }
                    serialized_friends.append(serialized_friend)
            return Response({"message": "You have these friends",
                             "friends": serialized_friends})
        return Response({"message": "You have No Friends"}, status=401)


class PostView:
    @api_view(['POST'])
    def getMainPagePosts(request):
        user_id = request.data['user_id']
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                friends = Friends.objects.filter(Q(from_user=user) | Q(to_user=user))
                friends_ids = [friend.from_user.id if friend.to_user == user else friend.to_user.id for friend in friends]
                posts = Posts.objects.filter(user__in=friends_ids)
                if posts.exists():
                    postsserialized = PostSerializer(posts, many=True)
                    return Response({"message": "Found these posts", "posts": postsserialized.data})
                return Response({"message": "No Posts Here","posts":[]}, status=200)

            except User.DoesNotExist:
                return Response({"message": "User not found"}, status=404)

        return Response({"message": "Invalid user_id provided"}, status=400)
    @api_view(['POST'])
    def makePost(request):
        user_id = request.data['user_id']
        caption = request.data['caption']
        image = request.data['image']
        user = User.objects.get(pk=user_id)
        if not User:
            return Response({"message": "No User Found"}, status=404)
        try:
            Posts.objects.create(user=user, caption=caption, image=image)
            return Response({"message": "Post Created"})
        except:
            return Response({"message": "Post Creation Failed"}, status=401)
    @api_view(['POST'])
    def likePost(request):
        user_id = request.data['user_id']
        post_id = request.data['post_id']
        user = User.objects.get(pk=user_id)
        if not user:
            return Response({"message": "Invalid User"}, status=401)
        post = Posts.objects.get(pk=post_id)
        if not post:
            return Response({"message": "Invalid Post"}, status=401)
        try:
            Likes.objects.create(user=user, post=post)
            post.no_of_likes+=1
            post.save()
            return Response({'message': 'Success'})
        except:
            return Response({"message": "Unexpected Error"}, status=401)