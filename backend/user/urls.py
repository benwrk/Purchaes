from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [

    url(r'^register', views.Register.as_view(), name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^profile/',views.user_profile,name='profile'),
    url(r'^', views.index, name='index'),
    url(r'^book/delete/$', views.delete, name='book-delete'),
    url(r'^book/update/$', views.update, name='book-update'),
    url(r'^book/', views.BookForm.as_view(), name='book'),
]
