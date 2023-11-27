# from django.shortcuts import render
from .models import Post
# from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post, Tags, Description
from .serializers import PostSerializer, TagsSerializer, DescriptionSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagsCreateView(generics.CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class TagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class DescriptionCreateView(generics.CreateAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class DescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class GetAllPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer