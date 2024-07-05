from django.urls import path

from blog.views import PostListView, PostSingleView, PostListByCategoryView, PostListByAuthorView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<str:slug>", PostSingleView.as_view(), name="post_detail"),
    path("category/<str:slug>", PostListByCategoryView.as_view(), name="category"),
    path("author/<str:slug>", PostListByAuthorView.as_view(), name="author"),
]
