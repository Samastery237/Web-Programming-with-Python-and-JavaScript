from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_request(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        pass_word = request.POST["password"]
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "users/login.html")

def logout_request(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "You have successfully logged out."
    })