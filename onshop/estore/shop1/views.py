from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product
from .forms import SignUpForm
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


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            
            user  = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been joined to our market!!!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again!!!"))
            return redirect('register')
    return render(request, 'registration/registration.html', {'form':form})