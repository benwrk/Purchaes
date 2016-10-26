from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50)


class Item(models.Model):
    CATEGORY = (
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
    description = models.CharField(max_length=500)
    time = models.TimeField(default=3000)
    tag = models.ManyToManyField(Tag)
    category = models.CharField(max_length=100,choices=CATEGORY)
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    def get_absolute_url(self):
        return reverse("api:detail", kwargs={'pk': self.pk})
