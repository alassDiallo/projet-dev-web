from django.shortcuts import render,redirect
from authentication.forms import Auth
from authentication.models import User

# Create your views here.


def authentification(request):
    #forms = Auth()

    if request.method=="POST":
        login = request.POST['login']
        password = request.POST['password']
        print(login,password)
        #user = User.objects.filter(
         #       login=login, password=password)

        #if len(user) == 1:
        #    request.session['login'] = login
        #    return redirect("home_page")
    return render(request,"authentification.html")


    
