from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home , name ='home'),
    path('contact', views.contact , name ='contact'),
    path('about', views.about, name ='about'),
    path('login', views.handlelogin, name ='login'),
    path('signup', views.handlesignup, name ='signup'),
    path('logout', views.handlelogout, name ='handlelogout'),
    path('addpost',views.addpost,name='addpost'),
    path('submit',views.submit,name='submit'),
    
]
