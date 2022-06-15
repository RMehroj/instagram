from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Like, UserFollowing


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_edited = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'is_edited', 'title', 'content',
                  'post_image', 'is_hidden', 'date_posted', 'like_set')


class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'following', 'followers']

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_edited = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'  # ['url', 'id', 'author', 'content']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class UserFollowingSerializer(serializers.ModelSerializer):
    following = serializers.ReadOnlyField(source='following_user_id.username')
    follower = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = UserFollowing
        fields = ['id', 'created', 'following', 'follower']


class FollowingSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='following_user_id.username')

    class Meta:
        model = UserFollowing
        fields = ['following_user_id', 'username', 'created']


class FollowersSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = UserFollowing
        fields = ['user_id', 'username', 'created']