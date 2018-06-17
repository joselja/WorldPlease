from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Post
from ads.permissions import PostPermissions
from ads.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer


class PostListAPI(ListCreateAPIView):
    """
    Posts list endpoint
    """
    queryset = Post.objects.all()
    permission_classes = [PostPermissions]

    def get_serializer_class(self):
        return NewPostSerializer if self.request.method == 'POST' else PostListSerializer

    def perform_create(self, serializer):
        serializer.save()


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Post detail endpoint
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [PostPermissions]


class UserPostListAPI(ListCreateAPIView):

    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.is_authenticated:
            return Post.objects
        else:
            return Post.objects
