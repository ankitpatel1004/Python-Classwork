from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        phone = data.get("phone")
        password = data.get("password")

        user = authenticate(request,phone=phone,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
             return render(request,"index.html",{"error":"Invalid credentials"})

    return render(request,"index.html")

def reg(request):
    roles = Role.objects.all()
    if request.method=='POST':
        data = request.POST
        role = Role.objects.get(id=data.get("role"))
        fname = data.get("firstname")
        lname = data.get("lastname")
        age = data.get("age")
        address = data.get("adr")
        phone = data.get("phone")
        password = data.get("password")     
        
        CustomeUser.objects.create_user(first_name=fname,last_name=lname,age=age,address=address,phone=phone,password=password,role=role)
        
        return render(request,"reg.html",{"roles":roles,"success":"Registration successfully"})
    
    roles = Role.objects.all()
    return render(request,"reg.html",{"roles":roles})

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return redirect("index")

def student(request):
    if request.user.is_authenticated and request.user.role.name == 'student':
        return render(request,"student.html")
    else:
        return render(request,"index.html")

def faculty(request):
    if request.user.is_authenticated and request.user.role.name == 'faculty':
        return render(request,"faculty.html")
    else:
        return render(request,"index.html")

