from django.shortcuts import render
from myapp.models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")
        Student.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{"msg":"Student added successfully"})
    return render(request,"index.html")
