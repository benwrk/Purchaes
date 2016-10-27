from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.



class Book(models.Model):
    book_id = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=100)
