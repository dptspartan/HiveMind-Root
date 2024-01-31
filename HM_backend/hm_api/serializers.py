from rest_framework import serializers
from .models import Posts
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"

    def get_username(self, obj):
        return obj.user.username