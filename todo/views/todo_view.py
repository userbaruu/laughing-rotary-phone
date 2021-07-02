from django.utils import timezone
from rest_framework import generics, permissions

from todo.models import Todo
from todo.serializers import TodoSerializer, TodoCompleteSerializer


class TodoCompletedListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Todo.objects\
            .filter(datecompleted__isnull=False, user=user)\
            .order_by('-datecompleted')


class TodoCollectionView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Todo.objects\
            .filter(datecompleted__isnull=True, user=user)\
            .order_by('-datecompleted')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TodoModification(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(datecompleted=timezone.now())
