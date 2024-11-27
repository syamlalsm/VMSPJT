
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.navbar,name='navbar'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('get-buildings/', views.get_buildings, name='get_buildings'),
    path('get-companies/', views.get_companies, name='get_companies'),
    path('visitor-form/', views.visitor_form, name='visitor_form'),
    path('submit-visitor-form/', views.submit_visitor_form, name='submit_visitor_form'),
]

    



    


     


   
