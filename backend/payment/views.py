from django.shortcuts import render
from items.models import Listing,Offer,Transaction
# Create your views here.
from django.views.generic import View
import hashlib,binascii



def payment(request):

    return render(request,'payment.html',{})

class seven_eleven(View):
    def get(self, request):
        return render(request, 'pay_by_711.html', {"code": str(hashlib.sha256("test".encode('utf-8')).hexdigest())[:25]})

    def post(self, request):
        if request.user.is_authenticated:
           offer_id = request.POST['offer_id']
           listing_id = request.POST['listing_id']
           return render(request,'pay_by_711.html',{"code":str(hashlib.sha256(("offer_id="+offer_id+",listing_id="+listing_id).encode('utf-8')).hexdigest())[:25],"offer_id":offer_id,"listing_id":listing_id})


def detail(request):
    id = request.GET.get('id', '')
    return render(request,'tranaction_detail.html',{"id":id})


class confirm(View):
    def get(self, request):
        return render(request, "successful.html")

    def post(self, request):
        if request.user.is_authenticated:
           offer_id = request.POST['offer_id']
           listing_id = request.POST['listing_id']
           offer = Offer.objects.get(id=offer_id)
           listing = Listing.objects.get(id=listing_id)
           listing.is_valid = False
           listing.save()
           offer.is_valid = False
           offer.save()
           tansaction = Transaction()
           tansaction.offer = offer
           tansaction.listing = listing
           tansaction.save()
           return render(request,"successful.html")