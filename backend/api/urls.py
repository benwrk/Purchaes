from django.conf.urls import url
from . import views

app_name = 'api'
urlpatterns = [
    url(r'^item/search$', views.item_search(), name='item-add'),
]
