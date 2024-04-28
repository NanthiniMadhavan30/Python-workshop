from django.urls import path, include
from .views import UserListCreateView, AllUserListView, UserUpdateView, UserDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/all', AllUserListView.as_view(), name='user-list-all'),
]
