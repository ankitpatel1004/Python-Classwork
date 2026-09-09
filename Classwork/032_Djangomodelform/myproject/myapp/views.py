from django.shortcuts import render,redirect
from myapp.forms import *
# Create your views here.

# def index(request):
#     form = StudentForm()
#     if request.method=='POST':
#         form = StudentForm(request.POST)
#         form.save()
#         return render(request,"index.html",{"form":form})
#     return render(request,"index.html",{"form":form})

def index(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        form.save()
        return redirect("index")
    return render(request,"index.html",{"form":form,"students":students})

def delete_std(request):
    id = request.GET['id']
    std = Student.objects.get(id=id)
    std.delete()
    return redirect("index")

def update_std(request):
    students = Student.objects.all()
    id = request.GET['id']
    std = Student.objects.get(id=id)
    if request.method=='POST':
        student = StudentForm(request.POST,instance=std)
        student.save()
        return redirect("index")

    form = StudentForm(instance=std)
    
    return render(request,"index.html",{"form":form,"students":students})