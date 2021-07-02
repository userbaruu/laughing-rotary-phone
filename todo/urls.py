from django.urls import path
from todo.views import base, todo_view

urlpatterns = [
   # Auth
   path('signup/', base.signupuser, name='signupuser'),
   path('login/', base.loginuser, name='loginuser'),
   path('logout/', base.logoutuser, name='logoutuser'),

   # Todos
   path('', base.home, name='home'),
   path('create/', base.createtodo, name='createtodo'),
   path('current/', base.currenttodos, name='currenttodos'),
   path('completed/', base.completedtodos, name='completedtodos'),
   path('todo/<int:todo_pk>', base.viewtodo, name='viewtodo'),
   path('todo/<int:todo_pk>/complete', base.completetodo, name='completetodo'),
   path('todo/<int:todo_pk>/delete', base.deletetodo, name='deletetodo'),

   # Api
   path('api/collection/', todo_view.TodoCollectionView.as_view()),
   path('api/collection/<int:pk>/', todo_view.TodoModification.as_view()),
   path('api/collection/<int:pk>/complete/', todo_view.TodoComplete.as_view()),
   path('api/completed/', todo_view.TodoCompletedListView.as_view()),
   path('api/signup/', todo_view.TodoCompletedListView.as_view()),
]
