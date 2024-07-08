from django import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, Prefetch
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment


class PostListView(generic.ListView):
    paginate_by = 1
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all().select_related("author", "category").annotate(comment_count=Count('comments'))
        if q := self.request.GET.get('q'):
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class PostListByCategoryView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return super().get_queryset().filter(category__slug=slug)


class PostListByAuthorView(PostListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        return super().get_queryset().filter(author__username=slug)


class PostSingleView(generic.DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(
            slug=slug
        ).select_related("author", "category").prefetch_related(
            Prefetch("comments", queryset=Comment.objects.select_related("author"))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class AddCommentView(LoginRequiredMixin, views.View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['comment']
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, 'Your comment has been successfully added ')
        else:
            messages.error(request, 'You comment has not been added')
        return redirect(f"{reverse('blog:post_detail', kwargs={'slug': post.slug})}#comments")


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return self.request.user == post.author

    def handle_no_permission(self):
        return redirect('blog:post_detail', slug=self.kwargs['slug'])


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author and request.method == "POST":
        messages.success(request, "Post has been successfully deleted")
        post.delete()
    return redirect(reverse_lazy('blog:post_list'))
