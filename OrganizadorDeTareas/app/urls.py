from django.contrib import admin
from django.urls import path, include
from app.views import *

app_name = "app"

urlpatterns = [
    path('', index,name='index'),
    path('registro', registerPage),
    path('landing',landing ,name='landing'),
    path('login', loginPage,name='login'),
    path('logout', logout_view,name='logout'),
    path('user-profile/', userProfile),
    path('user-security/', userSecurity),
    path('user-friends/', userFriends),
    path('user-activities/', userActivities),
]