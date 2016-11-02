from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    bio = models.TextField(max_length=1000)