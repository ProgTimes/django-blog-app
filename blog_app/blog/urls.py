from django.urls import path

from blog.views import BlogPostsView, BlogPostView

app_name = "blog"

urlpatterns = [
    path("", BlogPostsView.as_view(), name="post_list"),
    path("post/<str:slug>", BlogPostView.as_view(), name="post_detail"),
]
