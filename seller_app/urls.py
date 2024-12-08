from django.urls import path
from . import views
app_name = 'seller_app'
urlpatterns = [
    path('add_plant/', views.add_plant, name='add_plant'),
    path('delete_plant/<int:pk>/', views.delete_plant, name='delete_plant'),
    # Name should match exactly

]
