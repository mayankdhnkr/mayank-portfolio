from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('videoedits/', views.videoedits, name='videoedits'),
    path('designproject/', views.designpro, name='designproject'),
]