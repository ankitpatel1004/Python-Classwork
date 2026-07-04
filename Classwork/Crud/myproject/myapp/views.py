from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request,"index.html",{'categories':categories})

def create_product(request):
    if request.method == "POST":
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        price = data.get('price')
        qty = data.get('qty')
        cat = data.get('cat')
        category = Category.objects.get(id=cat)

        Product.objects.create(name=name,price=price,qty=qty,category=category)

    return render(request,"index.html",{'msg':'Product added successfully'})

def display_product(request):
    products = Product.objects.all()
    return render(request,"display.html",{'products':products})

def delete_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("display")
