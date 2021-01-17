from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User
# Create your views here.

def index(request):
    return render(request,"store/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "store/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "store/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        city=request.POST["city"]
        country=request.POST["country"]
        zip=request.POST["zip"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        #validation for Username

        if len(username) ==0:
            return render(request, "store/register.html", {
                "username_error": "Please Enter a Username."
            })
        if len(username) < 8:
            return render(request, "store/register.html", {
                "username_error": "Username must be greater than 8 characters."
            })
        if len(username) > 16:
            return render(request, "store/register.html", {
                "username_error": "username must be greater than 16 characters."
            })
        if not any(char.isdigit() for char in username):
            return render(request, "store/register.html", {
                "username_error": "username must have atleast one numeral."
            })
        if not any(char.isupper() for char in username):
            return render(request, "store/register.html", {
                "username_error": "username must have atleast one Uppercase Letter."
            })
        if not any(char.islower() for char in username):
            return render(request, "store/register.html", {
                "password_error": "Password must have atleast one lowercase Letter."
            })
        # validation for Password
        if len(password) < 8 :
            return render(request, "store/register.html", {
                "password_error": "Password must be greater than 8 characters."
            })
        if len(password) == 0 :
            return render(request, "store/register.html", {
                "password_error": "Please Enter a Password."
            })
        if len(password) > 16:
            return render(request, "store/register.html", {
                "password_error": "Password must be greater than 16 characters."
            })
        if not any(char.isdigit() for char in password):
            return render(request, "store/register.html", {
                "password_error": "Password must have atleast one numeral."
            })
        if not any(char.isupper() for char in password):
            return render(request, "store/register.html", {
                "password_error": "Password must have atleast one Uppercase Letter."
            })
        if not any(char.islower() for char in password):
            return render(request, "store/register.html", {
                "password_error": "Password must have atleast one lowercase Letter."
            })
        # checkcing if both passwords are equal
        if password != confirmation:
            return render(request, "store/register.html", {
                "password_error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username,password,email,first_name=first_name,last_name=last_name,city=city,country=country,zip=zip)
            user.save()
        except IntegrityError:
            return render(request, "store/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "store/register.html")

def cart(request):
    pass

def user_profile(request):
    args={'user':request.user}
    return render(request,"store/profile.html")