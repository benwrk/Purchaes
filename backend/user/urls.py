from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [

    url(r'^register', views.Register.as_view(), name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^profile/', views.user_profile, name='profile'),
    url(r'^redirect-login/', views.RedirectLoggingIn.as_view(), name='redirect-login'),
    url(r'^', views.index, name='index'),
]
