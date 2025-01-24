from django.urls import path
from .views import *
from . import views
app_name = 'account'
urlpatterns = [
    path('login/',views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('register/', views.registerpage, name='registerpage'),
    path('', views.home, name='home'),
    path('createcompany/', views.createcompany, name='createcompany'),
    path('createstaffaccount/', views.createstaffaccount, name='createstaffaccount'),
    path('user_update_view/<int:id>/', views.user_update_view, name='user_update_view'),


    path('reguseraccount/', views.reguseraccount, name='reguseraccount'),
]