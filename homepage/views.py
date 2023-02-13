from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'homepage/home.html')

def testt(request):
    return render(request, 'homepage/left.html')