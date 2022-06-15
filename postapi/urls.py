from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postapi import views as postapi_views

router = DefaultRouter()
router.register(r'posts', postapi_views.PostViewSet, basename='post')
router.register(r'comments', postapi_views.CommentViewSet, basename='comment')
router.register(r'likes', postapi_views.LikeViewSet, basename='like')
router.register(r'users', postapi_views.UserViewSet, basename='user')
router.register(r'userfollowings', postapi_views.UserFollowingViewSet, basename='userfollowing')

urlpatterns = [
    path('', include(router.urls)),
    path('users/follow/<int:pk>/', postapi_views.UserFollow.as_view(), name='user-follow'),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]