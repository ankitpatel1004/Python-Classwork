from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")
    
def register(request):
    if request.method=='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(name=name,email=email,age=age)
        return HttpResponse("Registration successfully")

def display(request):
    students = Student.objects.all()
    return JsonResponse({"data":list(students.values())})
    
def search(request):
    q = request.GET['q']
    students = Student.objects.filter(name__startswith=q) or Student.objects.filter(email__startswith=q) or Student.objects.filter(age__startswith=q)
    return JsonResponse({"data":list(students.values())})


def delete_student(request):
    id = request.GET['id']
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponse("Student deleted")

def retrive(request):
    id = request.GET['id']
    student = Student.objects.filter(id=id)
    return JsonResponse({"student":list(student.values())})

def update_student(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        student = Student.objects.get(id=id)
        student.name = name
        student.email = email
        student.age = age
        student.save()
        return HttpResponse("Update successfully")
        