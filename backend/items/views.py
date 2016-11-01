from django.shortcuts import render,redirect
from .models import Item, Tag
from django.views.generic import View
from user.models import User
from django.views.generic import DetailView
# Create your views here.

class item_create(View):
    model = Item
    fields = ['title', 'description']

    def get(self, request):
        return render(request, 'item_form.html')

    def post(self, request):
        if request.user.is_authenticated:
            title = request.POST['name']
            image_url = request.POST['image-url']
            image = request.FILES
            description = request.POST['description']
            time = request.POST['time']
            if Tag.objects.filter(title=request.POST['tag']).count() >0:
                tag = Tag.objects.get(title=request.POST['tag'])
            else:
                tag = Tag()
                tag.title = request.POST['tag']
                tag.save()
            print(tag)
            # category = models.CharField(max_length=100,choices=CATEGORY,default='none')
            category = request.POST['category']
            price_min = request.POST['price-min']
            price_max = request.POST['price-max']
            creator = User.objects.get(username=request.user.username)

            # image.url to get a url
            item = Item()
            item.title = title
            item.image_url =image_url
            item.image = image
            item.description = description
            item.time = time
            item.category = category
            item.price_min = price_min
            item.price_max = price_max
            item.creator = creator
            item.save()
            item.tag.add(tag)
        return redirect('item:item-detail')


def item_detail(request):
    id = request.GET.get('id', '')

    item = Item.objects.all()
    # if  id is  None:
    #     item =Item.objects.get(id=id)
    print(item)
    return render(request, 'item_detail.html', {'item': item})


class item_update(View):
    def get(self,request):
        if request.user.is_authenticated():
            id = request.GET.get('get','')
            user = request.user
            item = Item.objects.get(id=id)
            if user.name == item.creator:
                return render(request,'item_update.html',{'item':item})
            else:
                return render(request,'item_update.html',{})
        #alert to login
    def post(self,request):

        return redirect('item:detail')


def item_category(request):
    return None


def item_search(request):
    keyword = request.GET.get('keyword','')
    items = Item.objects.filter(title=keyword)
    items2 = Item.objects.filter(category=keyword)
    return render(request,'item_search.html',{'items':items})


def item_search_api(request):
    keyword = request.GET.get('keyword', '')
    items = Item.objects.filter(title=keyword)
    return {'items':items}

class item_offering(View):
    def get(self,request):
        return render(request,'item_offering.html')
    def post(self,request):
        return render(request,'item_offering.html')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


