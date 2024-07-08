from blog.models import Category, Post
from django import template

register = template.Library()


@register.inclusion_tag("blog/inc/_categories.html", name="categories")
def get_categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag("blog/inc/_recent_posts.html", name="recent_posts")
def recent_posts():
    posts = Post.objects.order_by("-created_at")[:3]
    return {"posts": posts}
