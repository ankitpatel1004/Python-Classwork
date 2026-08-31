from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout

# Create your views here.

def home(request):
    return render(request,"home.html")

def rooms(request):
    rooms = Room.objects.filter(available=True)
    return render(request,'rooms.html',{'rooms': rooms})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")

        return render(request,"login.html",{"err":"Invalid username or password"})

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmpassword")

        # Check passwords
        if password != confirm_password:
            return render(request, "register.html",{"err": "Password do not match"})

        # Check username
        if User.objects.filter(username=username).exists():
            return render(request, "register.html",{"err": "Username already exists"})

        # Create user
        User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,)
        return redirect("login")

    return render(request, "register.html")

def logout(request):
    auth_logout(request)
    return redirect("home")

def search_rooms(request):
    guests = request.GET.get('guests')
    room_type = request.GET.get('room_type')
    rooms = Room.objects.filter(available=True)

    # Filter by number of guests
    if guests:
        rooms = rooms.filter(capacity__gte=guests)

    # Filter by room type
    if room_type and room_type != "Any Room":
        rooms = rooms.filter(room_type=room_type)

    return render(request, 'search_results.html', {'rooms': rooms})
