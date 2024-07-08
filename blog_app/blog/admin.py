from blog.models import Category, Comment, Post
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "author",
    )
    readonly_fields = ("slug",)
    search_fields = (
        "title",
        "content",
    )
    list_filter = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "content",
        "author",
    )
