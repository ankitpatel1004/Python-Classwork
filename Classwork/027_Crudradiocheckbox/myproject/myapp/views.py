from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        gender = data.get("gender")
        lang = data.getlist("lang")
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
    id = request.GET['id']
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("display")

def update(request):
    id = request.GET['id']
    student =Student.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        student.name = data.get("name")
        student.email = data.get("email")
        student.password = data.get("password")
        student.gender = data.get("gender")
        lang = data.getlist("lang")
        student.country = data.get("country")
        student.address = data.get("address")
        l=""
        for i in lang:
            l+=i+","
        student.lang = l
        student.save()
        return render(request,"index.html",{"message":"Updated successfully"})

    return render(request,"index.html",{"student":student})
    