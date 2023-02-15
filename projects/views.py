from django.shortcuts import render
from .models import project
from datetime import datetime

# Create your views here.
now= datetime.now()
currdate = now.strftime("%B %d %Y")
currdate=currdate.upper()

def projects(request):
    projects=project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects, 'date':currdate})

def videoedits(request):
    projects=project.objects.all()
    return render(request, 'projects/videoedit.html', {'projects':projects, 'date':currdate})

def designpro(request):
    projects=project.objects.all()
    return render(request, 'projects/designpro.html', {'projects':projects, 'date':currdate})