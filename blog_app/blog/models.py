from django.db import models
from django.urls import reverse

from core.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} (by {self.author.username})"

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
