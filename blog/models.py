from django.db import models
from django.contrib.auth.models import User


def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id),
        title=str(instance.title), filename=filename)
    return file_path


class Post(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post", default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Order  our posts on the created_on field
        using descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title
