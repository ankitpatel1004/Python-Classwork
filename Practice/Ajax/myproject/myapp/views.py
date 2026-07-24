from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def test(request):
    q = request.GET['q']
    return HttpResponse(f"Hello {q}")

def search(request):
    q = request.GET['q']
    products = Product.objects.filter(name__startswith=q)
    data = "<ul>"
    for product in products:
        data+=f"<li>{product.name}</li>"
    data+="</ul>"
    return HttpResponse(data)

def collages(request):
    collages = Collage.objects.all()
    return JsonResponse({"data":list(collages.values())})

def departments(request):
    cid = request.GET['cid']
    departments = Department.objects.filter(collage_id=cid)
    return JsonResponse({"data":list(departments.values())})

def students(request):
    did = request.GET['did']
    students = Student.objects.filter(department_id=did)
    return JsonResponse({"data":list(students.values())})