from api.posts.models import Post
from rest_framework import filters
from api.posts.serializers import PostSerializer 
from rest_framework import generics
# from api.company.models import Company
from api.company.serializers import CompanySerializer

class GetAllPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class GetPostByRegisterId(generics.RetrieveAPIView):  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'register_id'

class GetPostByTag(generics.ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__language']

    def get_queryset(self):
        tag_language = self.kwargs['language']
        return Post.objects.filter(tags__language__icontains=tag_language)   
    
    
class GetPostByCity(generics.ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company__city'] 

    def get_queryset(self):
        city_id = self.kwargs['city']
        return Post.objects.filter(company__city=city_id)


class GetPostByCompany(generics.ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company__name__iexact']
 
    def get_queryset(self):
        company_name = self.kwargs['company_name']
        queryset = Post.objects.filter(company__name__iexact=company_name)
        return queryset