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

        if id:
            product = Product.objects.get(id=id)
            product.name = name
            product.price = price
            product.qty = qty
            product.category = category
            product.save()
            return render(request,"index.html")
        else:
            Product.objects.create(name=name,price=price,qty=qty,category=category)
            
    return redirect("display")

def display_product(request):
    products = Product.objects.all()
    return render(request,"display.html",{'products':products})

def delete_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("display")

def update_product(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,"index.html",{"product":product,"categories":categories,"products":products})