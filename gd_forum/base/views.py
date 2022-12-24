from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Thread, Category
from django.contrib.auth.models import User
# Create your views here.
def register_user (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'base/register.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')
    
def login_user(request):
    pass

def home (request):
    threads = Thread.objects.all()
    users = User.objects.all()
    categories = Category.objects.all()
    context = {
        'threads': threads,
        'users': users,
        'categories': categories,

    }
    return render(request, 'base/index.html', context)