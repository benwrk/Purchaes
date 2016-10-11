from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("api:detail", kwargs={'pk': self.pk})


class Book(models.Model):
    book_id = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    author = models.CharField(max_length=100)
