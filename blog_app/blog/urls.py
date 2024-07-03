from django.urls import path

from blog.views import BlogPostsView

urlpatterns = [
    path("", BlogPostsView.as_view(), name="blog_posts"),
]
