from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def market(request):
    return render(request,'market.html')