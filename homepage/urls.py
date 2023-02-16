from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('contactme/', views.contact, name='contactme'),
    path('experience/', views.experience, name='experience'),
]
