from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Thread, Category, Comment
from django.contrib.auth.models import User
from .forms import ThreadForm, RegisterUserForm
from django.db.models import Q
# Create your views here.
def register_user (request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    else:
        form = RegisterUserForm()
    return render(request, 'base/register.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.user.is_authenticated:
        return redirect( 'home' )
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if (User is not None):
            login(request, user)
            return redirect( 'home' )

        else:
            return messages.error(request, 'Username or password are incorrect')
    context = {}
    return render(request, 'base/login.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(Q(category__name__icontains=q) | Q(title__icontains=q) |  Q(uploader__username__icontains=q))
    users = User.objects.all()
    categories = Category.objects.all()
    context = {
        'threads': threads,
        'users': users,
        'categories': categories,

    }
    return render(request, 'base/index.html', context)

def thread(request, pk):
    thread = Thread.objects.get(id=pk)
    comments = thread.comment_set.all()
    if request.method == 'POST':
        comment = Comment.objects.create(
            uploader = request.user,
            thread = thread,
            text = request.POST.get('text')
        )
        return redirect('thread', thread.id)

    context = {
        'thread': thread,
        'comments': comments,
    }
    return render(request, 'base/thread.html', context)

def user_view(request, name):
    users = User.objects.get(username=name)
    context = {
        'users': users,
    }
    return render(request, 'base/user_view.html', context)

@login_required(login_url='login')
def create_thread(request):
    form = ThreadForm()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid:
            formID = form.save()
            return redirect('home')
    context = {
        'form': form,

    }
    return render(request, 'base/thread_form.html', context)

@login_required(login_url='login')
def edit_thread(request, pk):
    thread = Thread.objects.get(id=pk)
    form = ThreadForm(instance=thread)
    if request.user != thread.uploader:
        return redirect ('home')

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread', thread.id)
    context = {
        'form': form,
        'thread': thread,
    }
    return render(request, 'base/thread_form.html', context)

@login_required(login_url='login')
def delete_thread(request, pk):
    thread = Thread.objects.get(id=pk)
    if request.user != thread.uploader:
        return redirect ('home')

    if request.method == "POST":
        thread.delete()
        return redirect ( 'home' )
    return render(request, 'base/delete.html', {'obj': thread})

@login_required(login_url='login')
def delete_thread_no_warning(request, pk):
    thread = Thread.objects.get(id=pk)
    if request.user == thread.uploader:
        thread.delete()
        return redirect('home')
    else:
        return redirect('thread', thread.id)

@login_required(login_url='login')
def delete_comment_no_warning(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user == comment.uploader:
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')

@login_required(login_url='login')
def edit_username(request, name):
    user_name = User.objects.get(username=name)
    context = {
        'user_name': user_name,
    }
    if request.method == 'POST':
        if request.user == user_name:
            user_name.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'base/edit_user.html', context)