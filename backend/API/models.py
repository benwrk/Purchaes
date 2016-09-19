from django.db import models

# Create your models here.

class item(MOdels.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=300)
    description  = model.CharField(Max_length=500)
    tag = models.ManyToManyField(Tag)

class tag(Models.Model):
    title = models.CharField(max_length=50)
