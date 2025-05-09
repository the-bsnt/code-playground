from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("notes:dashboard"))
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register_user.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("notes:dashboard"))
            else:
                messages.error(request, f"Authentication Failed. Access Denied")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}:{error}")
    else:
        form = LoginForm()
    return render(request, "users/login_user.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("users:login_user")
