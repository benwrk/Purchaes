from django.shortcuts import render
from items.models import Listing
# Create your views here.
def index(request):
    return render(request,'index.html',{"listings":list(Listing.objects.all())[:6]})


def market(request):
    return render(request,'market.html')