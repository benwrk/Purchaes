from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    email = models.TextField(max_length=50,default="")
    bio = models.TextField(max_length=1000)

