from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=300)
    description  = models.CharField(max_length=500)
    tag = models.ManyToManyField(Tag)
