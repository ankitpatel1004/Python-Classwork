from django.shortcuts import render
from myapp.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def add_student(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')

        Student.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{"msg" : "Registration Successfully!..."})
    
    return render(request,"index.html")