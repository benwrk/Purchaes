from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    email = models.TextField(max_length=50,default="")
    bio = models.TextField(max_length=1000)

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
    
    def getTimeLeft(self):
        from datetime import datetime , timedelta

        unaware = datetime.now()
        created_date_test = (self.created_date + timedelta(hours=7)).replace(tzinfo=None)
        today = unaware.replace(tzinfo=None)
        time_dif = abs(today - created_date_test)
        time_dif_total_hour = time_dif.days * 24 + time_dif.seconds // 3600
        time_dif_total_second = time_dif.days * 24 * 3600 + time_dif.seconds
        if time_dif_total_hour >= self.valid_for:
            return 'Expired'
        else:
            remain_time_second = self.valid_for * 3600 - time_dif_total_second
            if remain_time_second > 24 * 3600:
                return str((remain_time_second // (24 * 3600))) + ' D ' + str((remain_time_second % (24 * 3600)) // 3600) + ' H'
            else:
                if remain_time_second > 3600:
                    return str(remain_time_second // 3600) + ' H ' + str((remain_time_second % 3600) // 60) + ' M'
                else:
                    if remain_time_second > 60:
                        return str(remain_time_second // 60) + ' M ' + str(remain_time_second % 60) + ' S'
                    else:
                        return str(remain_time_second) + ' S'      

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

