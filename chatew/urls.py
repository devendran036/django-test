from django.contrib import admin
from django.urls import path
from chatew import views
urlpatterns = [
    path('', views.home,name='home'),
    path('signup',views.create),
   
    
    path('login/',views.signin,name='login'),
    
    path('logout',views.logoutuser),
]
