from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product, Category
from .forms import SignUpForm
# Create your views here.


def category(request, foo):
    foo = foo.replace("-", " ").capitalize()
    try:
        category_obj = Category.objects.get(name=foo)  # Fetch specific category
        product = Product.objects.filter(category=category_obj)
        categories = Category.objects.all()  # Fetch all categories for the navbar
        return render(request, 'items/category.html', {
            'category': category_obj, 
            'product': product, 
            'categories': categories  # Pass all categories
        })
    except Category.DoesNotExist:
        messages.error(request, "Error in category name...")
        return redirect("home")


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products':products, 'categories':categories})


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'items/product.html', {"product":product})

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