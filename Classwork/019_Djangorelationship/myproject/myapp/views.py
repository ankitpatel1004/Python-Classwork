from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request,"index.html",{"categories" : categories})

def create(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        qty = data.get('qty')
        cat = data.get('cat')
        category = Category.objects.get(id=cat)

        Product.objects.create(name=name,price=price,qty=qty,category=category)

    return redirect("index")

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})
