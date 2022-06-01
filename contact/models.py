from django.db import models


STATUS = ((0, "Adcive"), (1, "Closed"))


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1500)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]
