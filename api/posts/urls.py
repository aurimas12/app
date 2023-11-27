from django.urls import path
from .views import (
    PostCreateView, 
    PostDetailView, 
    TagsCreateView, 
    TagsDetailView, 
    DescriptionCreateView, 
    DescriptionDetailView, 
    GetAllPosts
)


urlpatterns = [
    path('post/', PostCreateView.as_view(), name='company-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='company-detail'),
    
    path('tags/', TagsCreateView.as_view(), name='tags-create'),
    path('tags/<int:pk>/', TagsDetailView.as_view(), name='tags-detail'),  
    
    path('description/', DescriptionCreateView.as_view(), name='description-create'),
    path('description/<int:pk>/', DescriptionDetailView.as_view(), name='description-detail'),
    path('post/all/', GetAllPosts.as_view(), name='all_posts')
]
