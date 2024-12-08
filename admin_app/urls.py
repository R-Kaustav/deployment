from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.WelcomePage, name='WelcomePage'),
    path('user_app/', views.userprojecthomepage, name='UserProjectHomePage'),
    path('project/', views.projecthomepage, name='projecthomepage'),
    path('login/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('login_logic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('register/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('register_logic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('logout/', views.logout_view, name='logout'),
    path('seller/', views.seller_homepage, name='sellerhomepage'),
    path('taskreminder/', views.taskreminder, name='taskreminder'),
    path('gardenplanning/', views.gardenplanning, name='gardenplanning'),
    path('planttracker/', views.planttracker, name='planttracker'),
    path('gardeningtips/', views.gardeningtips, name='gardeningtips'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('forum/', views.forum, name='forum'),# This remains unchanged for admin app
]
