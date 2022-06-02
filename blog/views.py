from django.shortcuts import render
from .models import Post


def blog(request):
    """
    View all blog posts
    """
    posts = Post.objects.all()  # Get the post id
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
