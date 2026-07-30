from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method=="POST":
        data = request.POST
        phone = data.get('phone')
        password = data.get('password')
        user = authenticate(request,phone=phone,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"index.html",{'error':"Invalid credentails..."})
    return render(request,"index.html")

def reg(request):
    roles = Role.objects.all()
    if request.method == 'POST':
        data = request.POST
        role = Role.objects.get(id=data.get("role"))
        fname = data.get('firstname')
        lname = data.get('lastname')
        age = data.get('age')
        address = data.get('adr')
        phone = data.get('phone')
        password = data.get('password')

        CustomUser.objects.create_user(first_name=fname,last_name=lname,age=age,address=address,phone=phone,password=password,role=role)
        return render(request,"reg.html",{'roles':roles,"success":"Registration Successfully!"})

    roles = Role.objects.all()
    return render(request,"reg.html",{'roles':roles})

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")

def logout_url(request):
    logout(request)
    return redirect("index")

def buyer(request):
    if request.user.is_authenticated and request.user.role.name=='Buyer':
        return render(request,"buyer.html")
    else:
        return render(request,"index.html")

def seller(request):
    if request.user.is_authenticated and request.user.role.name=='Seller':
        return render(request,"seller.html")
    else:
        return render(request,"index.html")
        