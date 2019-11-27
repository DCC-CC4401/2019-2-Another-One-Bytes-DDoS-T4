from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', login),
    path('registro', register),
    path('landing', index),
    path('user-profile/', userProfile),
    path('user-security/', userSecurity),
    path('user-friends/', userFriends),
    path('user-activities/', userActivities),
]