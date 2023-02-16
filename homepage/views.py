from django.shortcuts import render
from .models import exp
from datetime import datetime

# Create your views here.

now= datetime.now()
currdate = now.strftime("%B %d %Y")
currdate=currdate.upper()

def home(request):
    return render(request, 'homepage/home.html', {'date':currdate,})

def contact(request):
    return render(request, 'homepage/contactme.html', {'date':currdate,})

def experience(request):
    exps=exp.objects.all()
    return render(request, 'homepage/experience.html', {'exps':exps,'date':currdate,})