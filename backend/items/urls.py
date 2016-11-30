from django.conf.urls import url
from . import views

app_name = 'item'
urlpatterns = [
    url(r'^add/$', views.item_create.as_view(), name='item-add'),
    url(r'^detail/$', views.item_detail,name='item-detail'),
    url(r'^edit/$',views.item_update.as_view(),name='item-update'),
    url(r'^category/$',views.item_category,name='item-category'),
    url(r'^offer-create/$', views.offer_create.as_view(), name='offer-create'),
    url(r'^offer-detail/$', views.offer_detail, name='offer-detail'),
    url(r'^offer-search/$',views.offer_search,name='offer-search'),
    url(r'^confirm/$',views.confirm,name="listing-confirm"),
    url(r'^search/$',views.item_search,name='item-search'),
]
