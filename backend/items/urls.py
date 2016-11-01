from django.conf.urls import url
from . import views

app_name = 'item'
urlpatterns = [
    url(r'^add/$', views.item_create.as_view(), name='item-add'),
    url(r'^detail/$', views.item_detail,name='item-detail'),
    url(r'^edit/$',views.item_update.as_view(),name='item-update'),
    url(r'^category/$',views.item_category,name='item-category'),
    url(r'^offering/$',views.item_offering.as_view(),name='item-offering'),
    url(r'^search/$',views.item_search,name='item-search'),
    url(r'^api/search',views.item_search_api,name='item-search-api')
]
