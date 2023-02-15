from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('webdev/', views.projects, name='webdev'),
    path('videoedits/', views.videoedits, name='videoedits'),
    path('designprojects/', views.designpro, name='designprojects'),
]