from django import views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentForm
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
        return Post.objects.filter(slug=slug).select_related("author", "category").prefetch_related("comments")

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
