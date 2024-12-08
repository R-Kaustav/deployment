from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'user_app'  # This sets the namespace for the app
urlpatterns = [
    path('homepage/', views.UserProjectHomePage, name='userprojecthomepage'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('weatherintegration/', views.weatherintegration, name='weatherintegration'),
    path('get-weather/', views.get_weather, name='get_weather'),
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),

    path('feedback/', views.feedback_form_view, name='feedback_form'),  # Feedback form page
    path('submit_feedback/', views.submit_feedback_view, name='submit_feedback'),  # Form submission
    path('thank-you/', lambda request: render(request, 'user_app/thank_you.html'), name='thank_you'),
    path('plant_tracker/', views.plant_tracker, name='plant_tracker'),
    # Thank You page


# Fixed the trailing space
]
