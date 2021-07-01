from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from posts.models import Post, Vote
from posts.serializers import PostSerializer, VoteSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class PostById(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        post = Post.objects.filter(pk=self.kwargs.get('pk'), poster=self.request.user)

        if post.exists():
            post.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            raise ValidationError({
                "detail": "Only owner can delete this...🙏"
            })


class VotePost(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs.get('pk'))

        return Vote.objects.filter(voter=user, post=post)

    def get_object(self):
        return self.get_queryset()

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError({
                "detail": "You already voted this post...🙏"
            })

        serializer.save(
            voter=self.request.user,
            post=Post.objects.get(pk=self.kwargs.get('pk'))
        )

    def perform_destroy(self, instance):
        vote = self.get_object()

        if vote.exists():
            vote.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return ValidationError({
                "detail": "Nothing found yet...🙏"
            })
