from django.db import models


# Models

class Category(models.Model):
    """Category Model"""
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=260)
    friendly_name = models.CharField(max_length=260, null=True, blank=True)
    objects = models.Manager()  # Object member

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name   # Display friendly name


class Product(models.Model):
    """Product Model"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    objects = models.Manager()  # Object member

    def __str__(self):
        return str(self.name)
