from django.shortcuts import render,redirect
from .models import Item
from django.views.generic import View
# Create your views here.

class item_create(View):
    model = Item
    fields = ['title', 'description']

    def get(self, request):
        Item.CATEGORY[0]
        return render(request, 'item_form.html', {'item':Item})

    def post(self, request):
        return render(request, 'index.htmk')


def item_detail(request):
    id = request.GET.get('id', '')
    item = Item.objects.get(id=id)
    return render(request,'item_detail',{'item':item})


class item_update(View):
    def get(self,request):
        return render(request,'item_update')
    def post(self,request):
        return redirect('item:detail')