from django.urls import path
from api.posts.views import GetAllPosts, GetPostByTag, GetPostByRegisterId, GetPostByCompany, GetPostByCity



urlpatterns = [
    path('posts/<str:all>/', GetAllPosts.as_view(), name='all_posts'),
    path('post/<int:register_id>/', GetPostByRegisterId.as_view(), name='get_post_by_id'),
    path('post/tags/<str:language>/', GetPostByTag.as_view(), name='get_posts_by_tag'),  # tag_name
    path('post/company/<str:company_name>/', GetPostByCompany.as_view(), name='get_post_by_company'),
    path('post/city/<str:city>/', GetPostByCity.as_view(), name='get_post_by_city')  # by id exp: vilnius = 1 id = 1
]
