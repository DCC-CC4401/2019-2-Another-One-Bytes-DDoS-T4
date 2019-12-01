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
    path('user-profile/', userProfile,name='userProfile'),
    path('user-profile/Avatar', userProfileAvatar,name='userProfileAvatar'),
    path('user-profile/Password', userProfilePassword,name='userProfilePassword'),
    path('user-security/', userSecurity,name='userSecurity'),
    path('user-friends/', userFriends,name='userFriends'),
    path('user-activities/', userActivities,name='userActivities'),
]