from django.urls import path
from api.posts.views import GetAllPosts, GetPostByTag, GetPostById, GetPostByCompany, GetPostByCity



urlpatterns = [
    path('post/all/', GetAllPosts.as_view(), name='all_posts'),
    path('post/<int:pk>/', GetPostById.as_view(), name='get_post_by_id'),
    path('post/tags/<str:language>/', GetPostByTag.as_view(), name='get_posts_by_tag'),  # tag_name
    path('post/company/<str:company_name>/', GetPostByCompany.as_view(), name='get_post_by_company'),
    path('post/city/<str:city_name>/', GetPostByCity.as_view(), name='get_post_by_city')
]
