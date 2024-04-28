from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserListCreateView(generics.ListCreateAPIView): # Retrieve & Write Only One Data from the table
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AllUserListView(generics.ListAPIView): # Retrieve All the Data from the table
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView): # Update only one Data from the table
    queryset = User.objects.all()
    serializer_class = UserSerializer
    partial = True