from django.shortcuts import render
from .models import Item
from django.views.generic import View
# Create your views here.

class item_create(View):
    model = Item
    fields = ['title', 'description']

    def get(self, request):
        return render(request, 'item_form.html', {})

    def post(self, request):
        return render(request, 'index.htmk');
