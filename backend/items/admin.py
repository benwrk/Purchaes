from django.contrib import admin

# Register your models here.
from .models import Item, Tag, Category, Listing, Transaction, Brand, Image

admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Transaction)
admin.site.register(Brand)
admin.site.register(Image)
