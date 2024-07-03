from django.contrib import admin

from blog.models import Post, Comment


@admin.register(Post)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author',)
    search_fields = ('title', 'content',)
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'author',)
