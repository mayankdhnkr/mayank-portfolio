from django.shortcuts import render
from datetime import datetime

# Create your views here.

now= datetime.now()
currdate = now.strftime("%B %d %Y")
currdate=currdate.upper()

def home(request):
    return render(request, 'homepage/home.html', {'date':currdate,})