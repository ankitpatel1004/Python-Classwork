from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})

def register(request):
    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("quantity")

        if id :
            product = Product.objects.get(id=id)
            product.name = name
            product.price = price
            product.qty = qty
            product.save()
            msg = "Update successfully"
        else:
            Product.objects.create(name=name,price=price,qty=qty)
            msg = "Registration successfully"
        return render(request,"index.html",{"msg":msg})

def delete(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("display")

def update(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    return render(request,"index.html",{"product":product})