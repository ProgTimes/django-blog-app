from django.urls import path

from blog.views import PostListView, PostSingleView, PostListByCategoryView, PostListByAuthorView, AddCommentView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<str:slug>", PostSingleView.as_view(), name="post_detail"),
    path("post/add-comment/<str:post_id>", AddCommentView.as_view(), name="add_comment"),
    path("category/<str:slug>", PostListByCategoryView.as_view(), name="category"),
    path("author/<str:slug>", PostListByAuthorView.as_view(), name="author"),
]
