from django.shortcuts import render
from education.forms import AddEducation

# Create your views here.


def addEducation(request):
    formEdu = AddEducation()

    return render(request,"addEducation.html",context={"forms":formEdu})
