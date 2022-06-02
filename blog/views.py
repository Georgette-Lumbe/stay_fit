from django.shortcuts import render
from .models import Post


def blog(request):
    """
    View all blog posts
    """
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
