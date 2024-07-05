from django.urls import path

from blog.views import PostListView, PostSingleView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<str:slug>", PostSingleView.as_view(), name="post_detail"),
    path("category/<str:slug>", PostSingleView.as_view(), name="category"),
]
