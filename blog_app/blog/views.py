from django.views import generic

from blog.models import Post


class BlogPostsView(generic.ListView):
    model = Post
    paginate_by = 1
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class BlogPostView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
