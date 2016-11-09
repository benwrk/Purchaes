from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.views.generic import View
from user.models import User
from itertools import chain

from django.views.generic import DetailView
# Create your views here.
def tag_check(input):
    print(input)
    try:
        print('1')
        tag =  Tag.objects.get(name=input)
        print(tag)
    except Tag.DoesNotExist:
        print('0')
        tag = Tag()
        tag.name = input
        tag.save()
    return tag

def brand_check(name):
    if Brand.objects.filter(name=name).count() > 0:
        return Brand.objects.get(name=name)
    else:
        brand = Brand()
        brand.name = name
        brand.save()
        return brand
def category_check(name):
    if Category.objects.filter(name=name).count() > 0:
        return Category.objects.get(name=name)
    else:
        category = Category()
        category.name = name
        category.save()
        return category

def custom_redirect(url_name, parameter ):
    from django.core.urlresolvers import reverse
    import urllib
    url = reverse(url_name)

    return HttpResponseRedirect(url + "?%s" % parameter)

class item_create(View):
    model = Item
    fields = ['title', 'description']

    def get(self, request):
        return render(request, 'item_form.html',{'items':Item.objects.all(),"brands":Brand.objects.all()})

    def post(self, request):
        if request.user.is_authenticated:
            if Item.objects.filter(name=request.POST['name']).count() > 0:
                item = Item.objects.get(name=request.POST['name'])
            else:
                item = Item()
                item.name = request.POST['name']
                item.description = request.POST['description-item']
                item.brand = brand_check(request.POST['brand'])
                item.category = category_check(request.POST['category'])
                item.tags.add(tag_check(request.POST['tag-item']))
                item.save()
                if len(request.FILES.getlist('image'))>0:
                    for i in  request.FILES.getlist('image'):
                        image = Image()
                        image.image = i
                        image.save()
                        item.image.add(image)
                else:
                    image = Image()
                    image.image = request.FILES.get('image')
                    image.save()
                    item.image.add(image)


            listing = Listing()
            listing.valid_for = request.POST['valid_for']
            listing.title = request.POST['title']
            listing.description = request.POST['description']
            listing.item = item
            listing.owner = User.objects.get(username=request.user.username)
            listing.max_accepted_price = request.POST['max_accepted_price']
            listing.save()
            listing.tags.add = tag_check(request.POST['tag-listing'])
            return custom_redirect('item:item-detail' , 'id='+str(listing.id))
        return redirect('item:item-add')

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
        return custom_redirect('item:item-detail','id='+str(listing.id))


def item_category(request):
    return None


def item_search(request):
    keyword = request.GET.get('keyword','')
    category = request.GET.get('category','')
    if keyword =='':
        listings = Listing.objects.filter( item__in=Item.objects.filter(category__name=category))
    elif category == 'All':
        listings = Listing.objects.filter(title=keyword)
    else:
        listings = Listing.objects.filter(title=keyword,item__in=Item.objects.filter(category__name=category))
    items = Item.objects.filter(category__name=keyword)
    tag = Listing.objects.filter(tag)
    # list =
    print(type(list))
    # print (Item.objects.filter(category__name=category))
    # print (category)
    # print(type(listings))
    # listings = set(listings)
    # print(listings)
    # print(type(listings))
    # listings = list(listings)
    # print(listings)
    # print(type(listings))
    # print (items)
    return render(request,'item_search.html',{'listings':listings.all(),'items':items})

class offer_create(View):
    def get(self,request):
        id = None
        if request.GET.get('id','') is not None:
            id = request.GET.get('id','')
        return render(request,'offer_create.html',{"id":id,'listings':Listing.objects.all()})
    def post(self,request):
        if request.user.is_authenticated:
            # if not Offer.objects.filter(title=request.POST['title']).count()>0:
            offer = Offer()
            offer.valid_for = request.POST['valid_for']
            offer.title = request.POST['title']
            offer.description = request.POST['description']
            offer.listing = Listing.objects.get(id= request.POST['listing-id'])
            offer.owner = User.objects.get(username=request.user.username)
            offer.price = request.POST['price']
            offer.save()
            if len(request.FILES.getlist('image')) > 0:
                for i in request.FILES.getlist('image'):
                    image = Image()
                    image.image = i
                    image.save()
                    offer.image.add(image)
            else:
                print('in',request.FILES.get('image'))
                image = Image()
                image.image = request.FILES.get('image')
                image.save()
                offer.image.add(image)
            offer.tags.add(tag_check(request.POST['tag']))

            return custom_redirect('item:offer-detail' , 'id='+str(offer.id))
            # else:
            #     return custom_redirect('item:offer-detail', 'id=' + str(Offer.objects.get(title=request.POST['title']).id))
def offer_detail(request):
    offer = Offer.objects.get(id=request.GET.get('id',''))
    return render(request,'offer_detail.html',{"offer":offer})

def offer_search(request):
    id = request.GET.get('id','')
    offers=Offer.objects.filter(listing_id=id)
    return render(request,'offer_search.html',{'offers':offers})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

