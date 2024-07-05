from django.db.models import Count
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    paginate_by = 10
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().select_related("author", "category").annotate(comment_count=Count('comment'))


class PostListByCategoryView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return super().get_queryset().filter(category__slug=slug)


class PostListByAuthorView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return super().get_queryset().filter(author__username=slug)


class PostSingleView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
