from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(name='menu_items')
def menu_items():
    return {
        'Home': reverse('blog:post_list'),
        'Login': reverse('user:login'),
    }
