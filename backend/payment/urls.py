from django.conf.urls import url
from . import views

app_name = 'payment'
urlpatterns = [
    # url(r'^omise/$', views.item_create.as_view(), name='item-add'),
    url(r'^', views.payment, name='payment'),

]
