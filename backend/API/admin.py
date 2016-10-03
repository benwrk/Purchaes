from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Tag,Item,Book
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Book)