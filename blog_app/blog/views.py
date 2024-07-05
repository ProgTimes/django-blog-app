from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 1
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostListByCategoryView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(category__slug=slug)


class PostListByAuthorView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(author__username=slug)


class PostSingleView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
