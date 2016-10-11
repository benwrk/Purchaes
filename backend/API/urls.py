from django.conf.urls import url
from . import views

app_name = 'api'
urlpatterns = [

    url(r'^register', views.UserFormView.as_view(), name='register'),
    url(r'^item/add/$', views.ItemCreate.as_view(), name='item-add'),
    url(r'^book/delete/$', views.delete, name='book-delete'),
    url(r'^book/update/$', views.update, name='book-update'),
    url(r'^book/', views.BookForm.as_view(), name='book'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^', views.index, name='index'),
]
