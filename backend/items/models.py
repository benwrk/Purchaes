from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50)


class Item(models.Model):
    CATEGORY = (
        ('none','None'),
        ('Electronic',
         ('computer', 'Computer')),
        ('cloth', 'Cloth'),
        ('sport', 'Sport'),
        ('home', 'Home'),
        ('fresh', 'Fresh'),
        ('tools', 'Tools'),
    )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=300)
    image = models.FileField(upload_to='upload/',default='static/images/1x1x100.png')
    description = models.CharField(max_length=500)
    time = models.TimeField(default=3000)
    tag = models.ManyToManyField(Tag)
    # category = models.CharField(max_length=100,choices=CATEGORY,default='none')
    category = models.CharField(max_length=100,default='none')
    price_min = models.IntegerField(default=0)
    price_max = models.IntegerField(default=10000000)
    creator = models.ForeignKey('user.User',default=1)

    def get_absolute_url(self):
        return reverse("item:detail", kwargs={'pk': self.pk})
