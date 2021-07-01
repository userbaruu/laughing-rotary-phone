from django.urls import path
from posts.views import PostList, PostById, VotePost

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostById.as_view()),
   path('<int:pk>/vote/', VotePost.as_view()),
]
