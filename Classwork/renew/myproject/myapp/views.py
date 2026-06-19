from django.shortcuts import render
from myapp.models import *

# Create your views here.

def index(request):
    return render (request,"index.html")

def display(request):
    if request.method == "POST":
        data = request.POST
        productname = data.get('productname')
        price = data.get('price')
        quantity = data.get('quantity')

        Product.objects.create(productname=productname,price=price,quantity=quantity)
        return render(request,"index.html",{'msg' : 'Product added successfully'})

    return render(request,"index.html")