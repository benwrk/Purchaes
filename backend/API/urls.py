from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^', views.index),
]