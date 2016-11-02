from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.views.generic import View
from user.models import User

from django.views.generic import DetailView
# Create your views here.
def tag_check(input):
    if Tag.objects.filter(title=input).count() > 0:
        return Tag.objects.get(title=input)
    else:
        tag = Tag()
        tag.title = input
        tag.save()
        return tag
def category_check(name):
    if Category.objects.filter(title=name).count() > 0:
        return Category.objects.get(title=name)
    else:
        category = Category()
        category.name = name
        category.save()
        return category

def custom_redirect(url_name, *args, **kwargs):
    from django.core.urlresolvers import reverse
    import urllib
    url = reverse(url_name, args = args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)

class item_create(View):
    model = Item
    fields = ['title', 'description']

    def get(self, request):
        return render(request, 'item_form.html')

    def post(self, request):
        if request.user.is_authenticated:
            if Item.objects.filter(name=request.POST['name']).count() > 0:
                item = Item.objects.get(name=request.POST['name'])
            else:
                item = Item()
                item.name = request.POST['name']
                item.description = request.POST['description-item']
                item.brand = request.POST['description']
                item.category = category_check(request.POST['category'])
                item = Item()
                if len(request.FILES.getList('image'))>0:
                    for i in  request.FILES.getList('image'):
                        image = Image()
                        image.image = i
                        image.save()
                        item.image.add(image)
                else:
                    image = Image()
                    image.image = request.FILES.get('image')
                    image.save()
                    item.image.add(image)
                item.tags.add(tag_check(request.POST['tag-item']))

            listing = Listing()
            listing.valid_for = request.POST['valid_for']
            listing.title = request.POST['title']
            listing.description = request.POST['description-listing']
            listing.item = item
            listing.owner = User.objects.get(username=request.user.username)
            listing.max_accepted_price = request.POST['max_accepted_price']
            listing.save()
            listing.tags.add = tag_check(request.POST['tag-listing'])
            return custom_redirect('item:item-detail' , id = listing.id)
        return redirect('item-item-create')

def item_detail(request):
    i= request.GET.get('id', '')
    listing = Listing.objects.get(id=i)
    print(id)
    print(listing)

    return render(request, 'item_detail.html', {'listing': listing})

class item_update(View):
    def get(self,request):
        if request.user.is_authenticated():
            id = request.GET.get('id','')
            user = request.user
            item = Listing.objects.get(id=id)
            if user.name == item.creator:
                return render(request,'item_update.html',{'item':item})
            else:
                return render(request,'item_update.html',{})
        #alert to login
    def post(self,request):
        listing = Listing.objects.get(id=request.POST[id])
        listing.valid_for = request.POST['valid_for']
        listing.title = request.POST['title']
        listing.description = request.POST['description-listing']
        return custom_redirect('item:item-detail','',id=listing.id)


def item_category(request):
    return None


def item_search(request):
    keyword = request.GET.get('keyword','')
    listings = Listing.objects.filter(title=keyword)
    items = Item.objects.filter(category=keyword)
    return render(request,'item_search.html',{'listings':listings,'item':items})

class offer_create(View):
    def get(self,request):
        id = 0
        if request.GET.get('id','') is not None:
            id = request.GET.get('id','')
        return render(request,'offer_create.html',{"id":id})
    def post(self,request):
        if request.user.is_authenticated:
            offer = Offer()
            offer.valid_for = request.POST['valid_for']
            offer.title = request.POST['title']
            offer.description = request.POST['description']
            offer.listing = Listing.objects.get(id= request.POST['listing-id'])
            offer.owner = User.objects.get(username=request.user.username)
            offer.price = request.POST['price']
            offer.save()
            if len(request.FILES.getList('image')) > 0:
                for i in request.FILES.getList('image'):
                    image = Image()
                    image.image = i
                    image.save()
                    offer.image.add(image)
            else:
                image = Image()
                image.image = request.FILES.get('image')
                image.save()
                offer.image.add(image)
            offer.tags.add(tag_check(request.POST['tag-item']))
            return render(request,'offer_detail.html',{'offer':offer})
def offer_detail(request):
    offer = Offer.objects.get(id=request.GET.get('id',''))
    return render(request,'offer_detail.html',{"offer":offer})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


