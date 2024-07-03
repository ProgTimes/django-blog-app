from django.views import generic

from blog.models import Post


class BlogPostsView(generic.ListView):
    template_name = 'blog/blog_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()
