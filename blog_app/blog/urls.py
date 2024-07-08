from django.urls import path

import blog.views as blog_views

app_name = "blog"

urlpatterns = [
    path("", blog_views.PostListView.as_view(), name="post_list"),
    path("post/<str:slug>", blog_views.PostSingleView.as_view(), name="post_detail"),
    path("post/<str:slug>/edit", blog_views.PostUpdateView.as_view(), name="edit_post"),
    path("post/<str:slug>/delete", blog_views.delete_post, name="delete_post"),
    path("post/add-comment/<str:post_id>", blog_views.AddCommentView.as_view(), name="add_comment"),
    path("category/<str:slug>", blog_views.PostListByCategoryView.as_view(), name="category"),
    path("author/<str:slug>", blog_views.PostListByAuthorView.as_view(), name="author"),
]
