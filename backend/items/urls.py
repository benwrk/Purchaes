from django.conf.urls import url
from . import views

app_name = 'item'
urlpatterns = [
    url(r'^add/$', views.item_create.as_view(), name='item-add'),
    url(r'^detail/$', views.item_detail,name='item-detail'),
    url(r'^edit/$',views.item_update,name='item-update')
]
