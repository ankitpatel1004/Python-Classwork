from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request,"index.html",{"categories" : categories})

def create(request):
    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get('name')
        price = data.get('price')
        qty = data.get('qty')
        cat = data.get('cat')
        category = Category.objects.get(id=cat)

        if id:
            products = Product.objects.get(id=id)
            products.name = name
            products.price = price
            products.qty = qty
            products.category = category
            products.save()
            return render(request,"index.html",{'msg':'Product update successfully'})
        else:
            Product.objects.create(name=name,price=price,qty=qty,category=category)
            return render(request,"index.html",{'msg':'Product added successfully'})

    return redirect("index")

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})

def delete(request):
    id = request.GET['id']
    products = Product.objects.get(id=id)
    products.delete()
    return redirect("display")

def update(request):
    id = request.GET['id']
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    product = Product.objects.all()
    return render(request,"index.html",{'product':product,'categories':categories,'product':product})