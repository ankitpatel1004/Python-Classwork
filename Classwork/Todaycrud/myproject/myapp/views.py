from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def add_student(request):
    if request.method == "POST":
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')

        if id:
            student=Student.objects.get(id=id)
            student.name=name
            student.email=email
            student.age=age
            student.save()
            return render(request,"index.html",{"msg":"Updated successfully"})
        else:
            Student.objects.create(name=name,email=email,age=age)
            return render(request,"index.html",{"msg":"Registration successfully"})
    
def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{"students":students})

def delete(request):
    id = request.GET.get("id")
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("display")

def update(request):
    id = request.GET.get("id")
    student = Student.objects.get(id=id)
    return render(request,"index.html",{"student":student})
    