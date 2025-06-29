from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms
from . import models
import time


# Create your views here.
def login_user(request):
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")
    else:
        return render(request, "access/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("login")


def register_user(request):
    if request.method == "POST":
        user_creation = forms.RegisterForm(request.POST)
        if user_creation.is_valid():
            user_creation.save()
            name = user_creation.cleaned_data["username"]
            password = user_creation.cleaned_data["password1"]
            user = authenticate(request, username=name, password=password)
            login(request, user)
            time.sleep(0.3)
            return redirect("home")
        else:
            messages.success(request, "There is error in credentials use different")
            user_creation = forms.RegisterForm()
        return render(request, "access/register.html", {"form": user_creation})
    else:
        user_creation = forms.RegisterForm()
        return render(request, "access/register.html", {"form": user_creation})


def home(request):
    data = models.Posts.objects.all()
    return render(request, "access/home.html", {"data": data})


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        create_post = forms.CreatePostForm(request.POST, request.FILES)
        if create_post.is_valid():
            create_post.save()
        return redirect("home")
    else:
        create_post = forms.CreatePostForm()
        return render(request, "access/create_post.html", {"form": create_post})


@login_required(login_url="login")
def view_post(request, pk):
    data = models.Posts.objects.all(id=pk)
    return render(request, "access/post.html", {"data": data})
