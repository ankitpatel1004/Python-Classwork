from django.shortcuts import render,redirect
from myapp.forms import *

# Create your views here.

def index(request):
    form = EmployeeForm()
    emp = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        return redirect("index")
    return render(request,"index.html",{"form":form,"emp":emp})

def delete_emp(request):
    id = request.GET['id']
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect("index")

def update_emp(request):
    emp = Employee.objects.all()
    id = request.GET['id']
    e = Employee.objects.get(id=id)
    if request.method=='POST':
        emp = EmployeeForm(request.POST,instance=e)
        emp.save()
        return redirect("index")

    form = EmployeeForm(instance=e)
    
    return render(request,"index.html",{"form":form,"e":e})
    