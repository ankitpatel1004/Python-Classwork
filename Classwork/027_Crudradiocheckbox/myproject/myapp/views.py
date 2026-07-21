from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        gender = data.get("gender")
        lang = data.get("lang")
        country = data.get("country")
        address = data.get("address")
        l = ""
        for i in lang:
            l+=i+","
        Student.objects.create(name=name,email=email,password=password,gender=gender,lang=l,country=country,address=address)
        return render(request,"index.html",{"message":"Registration successfully"})

    return render(request,"index.html")

def display(request):
    students = Student.objects.all()
    for st in students:
        st.lang = st.lang.split(",")
    return render(request,"display.html",{"students":students})

def delete(request):
    return render(request,"display.html")

def update(request):
    return render(request,"display.html")