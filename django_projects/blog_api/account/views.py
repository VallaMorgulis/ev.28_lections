from dj_rest_auth.views import LogoutView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from django.core.paginator import Paginator


from comment.serializers import CommentSerializer
from like.serializers import FavoriteSerializer
# from posts.models import Post
from posts.serializers import PostListLikesSerializer
from . import serializers


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer
        return serializers.UserDetailSerializer

    @action(['GET'], detail=True)
    def favorites(self, request, pk):
        user = self.get_object()
        fav_posts = user.favorites.all()
        serializer = FavoriteSerializer(fav_posts, many=True)
        return Response(serializer.data, status=200)

    @action(['GET'], detail=True)
    def comments(self, request, pk=None):
        user = self.get_object()
        comments = user.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    @action(['GET'], detail=True)
    def liked_posts(self, request, pk=None):
        user = self.get_object()
        liked_posts = user.likes.all()
        # post_ids = liked_posts.values_list('post_id', flat=True)
        # posts = Post.objects.filter(id__in=post_ids)
        posts = [like.post for like in liked_posts]
        # paginator = Paginator(posts, 3)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        serializer = PostListLikesSerializer(posts, many=True)
        return Response(serializer.data, status=200)

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserDetailSerializer
#     permission_classes = (permissions.IsAuthenticated,)
