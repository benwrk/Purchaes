"""Purchaes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from app import views

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.item_create.as_view(), name='item-add'),
    url(r'^detail/$', views.item_detail, name='item-detail'),
    url(r'^edit/$', views.item_update.as_view(), name='item-update'),
    url(r'^category/$', views.item_category, name='item-category'),
    url(r'^offer-create/$', views.offer_create.as_view(), name='offer-create'),
    url(r'^offer-detail/$', views.offer_detail, name='offer-detail'),
    url(r'^offer-search/$', views.offer_search, name='offer-search'),
    url(r'^search/$', views.item_search, name='item-search'),
    url(r'^register', views.Register.as_view(), name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^redirect-login', views.RedirectLoggingIn.as_view(), name='redirect-login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^profile/', views.user_profile,name='profile')
]
