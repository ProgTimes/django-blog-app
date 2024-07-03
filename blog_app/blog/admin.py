from blog.models import Post
from django.contrib import admin


@admin.register(Post)
class BeerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
