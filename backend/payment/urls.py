from django.conf.urls import url
from . import views

app_name = 'payment'
urlpatterns = [
    # url(r'^omise/$', views.item_create.as_view(), name='item-add'),
    url(r'^detail',views.detail,name="detail"),
    url(r'^7-11',views.seven_eleven.as_view(), name="7-11" ),
    url(r'^confirm',views.confirm.as_view(),name="confirm"),
    url(r'^', views.payment, name='payment'),

]
