from django.urls import path
from .views import UserView, FriendsView

urlpatterns = [
    path('login/', UserView.login_user, name='login_user'),
    path('logout/', UserView.logout_user, name='logout_user'),
    path('register/', UserView.register_user, name='register_user'),
    path('friendRequest/', FriendsView.send_friend_request, name='send_friend_request')
]