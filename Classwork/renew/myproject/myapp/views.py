from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    return render (request,"index.html")

def create(request):
    if request.method == "POST":
        data = request.POST
        id = data.get('id')
        productname = data.get('productname')
        price = data.get('price')
        quantity = data.get('quantity')

        if id:
            product = Product.objects.get(id=id)
            product.productname = productname
            product.price = price
            product.quantity = quantity
            product.save()
            return render(request,"index.html",{'msg' : 'Product Updated successfully'})
        
        else:
            Product.objects.create(productname=productname,price=price,quantity=quantity)
            return render(request,"index.html",{'msg' : 'Product added successfully'})

    return render(request,"index.html")

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{'products':products})

def delete(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("display")

def update(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    return render(request,"index.html",{'product':product})

