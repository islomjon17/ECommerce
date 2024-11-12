from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})




def about(request):
   
    return render(request, 'about.html')



def login_user(request):
    if request.method == "POST":
        username =  request.POST['username']
        password =  request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You heve been Loged in!!!!"))
            return redirect("home")
        else:
            messages.success(request, ("There was an error please try egain!!!!"))
            return redirect("login")
    else:
        return render(request, 'registration/login.html', {})
    



def logout_user(request):
    logout(request)
    messages.success(request, ("You heve been Loged out!!!!"))
    return redirect("home")