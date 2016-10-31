from django.shortcuts import render,redirect
from .models import Item
from django.views.generic import View
from django.views.generic import DetailView
# Create your views here.

class item_create(View):
    model = Item
    fields = ['title', 'description']

    def get(self, request):
        return render(request, 'item_form.html')

    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        tag = request.POST['tag']
        category = request.POST['category']
        name = request.POST['name']
        name = request.POST['name']
        return redirect('item:item-detail')


def item_detail(request):
    id = request.GET.get('id', '')
    item = Item.objects.get(id=id)
    return repr(render(request, 'item_detail.html', {'item': item}))


class item_update(View):
    def get(self,request):
        if request.user.is_authenticated():
            id = request.GET.get('get','')
            user = request.user
            item = Item.objects.get(id=id)
            return render(request,'item_update.html',{'item':item})
        #alert to login
    def post(self,request):
        return redirect('item:detail')


def item_category(request):
    return None


def item_search(request):
    return render(request,'item_search.html',{'item':Item.objects})


class item_offering(View):
    def get(self,request):
        return render(request,'item_offering.html')
    def post(self,request):
        return render(request,'item_offering.html')