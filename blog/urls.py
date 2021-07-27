from django.urls import path
from blog.views import (
    blog_view,
    blog_post_detail,
    detail_blog_view,

)

app_name = 'blog'

urlpatterns = [
    path('blog/', blog_view, name="blog"),
    path('post_detail/', blog_post_detail, name="postDetail"),
    path('<slug:slug>/', detail_blog_view, name="detail"),
    # path('<slug>/edit/', edit_blog_view, name="edit"),

]
