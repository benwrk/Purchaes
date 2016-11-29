from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^market',views.market,name='market'),
    url(r'^', views.index, name='home'),
]
