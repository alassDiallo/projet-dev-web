from django.http import HttpResponse
from django.shortcuts import render
from education.models import Education

# Create your views here.

def index(request):
    educations = Education.objects.all()
    
    return render(request,"accueil.html",context={'educations':educations})

