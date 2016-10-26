from django.conf.urls import url
from . import views

app_name = 'item'
urlpatterns = [
    url(r'^add/$', views.item_create.as_view(), name='item-add'),
]
