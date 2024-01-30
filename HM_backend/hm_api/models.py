from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_user', 'to_user'], name='unique_friend_request')
        ]


class Friends(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_1', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_user', 'to_user'], name='unique_friends')
        ]

class Posts(models.Model):
    user = models.ForeignKey(User, related_name='user_who_posted', on_delete=models.CASCADE)
    caption = models.TextField(null=False)
    image = models.ImageField(upload_to='images/')
    no_of_likes = models.IntegerField(default=0)

class Likes(models.Model):
    user = models.ForeignKey(User, related_name='user_who_liked', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='post_liked', on_delete=models.CASCADE)