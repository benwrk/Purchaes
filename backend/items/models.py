from django.db import models
from django.core.urlresolvers import reverse

from django.db import models
from django.db import models
from user.models import User
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50,unique=True)

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/', default='static/images/1x1x100.png')

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey(Category)
    image = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)

class Listing(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    valid_for = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    item = models.ForeignKey(Item)
    owner = models.ForeignKey(User)
    max_accepted_price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag)

class Offer(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    valid_for = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    listing = models.ForeignKey(Listing)
    owner = models.ForeignKey(User)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)

class Transaction(models.Model):
    committed_date = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing)
    offer = models.ForeignKey(Offer)

