from django.conf.urls import url
from . import views

app_name = 'item'
urlpatterns = [
    url(r'^$', views.index(), name='item-add'),

]
