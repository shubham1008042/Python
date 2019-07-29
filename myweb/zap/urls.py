from django.contrib import admin
from django.conf.urls import url,include
# from django.contrib.auth.views import LoginView
from . import views

# SET THE NAMESPACE!


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register',views.usersignup,name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.account, name='activate'),  
    url(r'^login/',views.userlogin,name='login'),
    url(r'^special',views.special,name='special'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]