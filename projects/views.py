from django.shortcuts import render
from .models import project
# Create your views here.

def projects(request):
    projects=project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def videoedits(request):
    projects=project.objects.all()
    return render(request, 'projects/videoedit.html', {'projects':projects})

def designpro(request):
    projects=project.objects.all()
    return render(request, 'projects/designpro.html', {'projects':projects})