from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Transaction)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Offer)