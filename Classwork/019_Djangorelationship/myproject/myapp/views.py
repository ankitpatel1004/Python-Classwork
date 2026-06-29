from django.shortcuts import render,redirect
from myapp.models import *
import os
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
        image = request.FILES.get("image")

        if id:
            products = Product.objects.get(id=id)
            products.name = name
            products.price = price
            products.qty = qty
            products.category = category
            if request.FILES:
                if products.image:
                    os.remove(products.image.path)
                products.image = image
            products.save()
            return render(request,"index.html",{'msg':'Product update successfully'})
        else:
            Product.objects.create(name=name,price=price,qty=qty,category=category,image=image)
            return render(request,"index.html",{'msg':'Product added successfully'})

    return redirect("index")

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})

def delete(request):
    id = request.GET['id']
    products = Product.objects.get(id=id)
    os.remove(products.image.path)
    products.delete()
    return redirect("display")

def update(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST['id'])
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.qty = request.POST['qty']
        product.category = Category.objects.get(id=request.POST['cat'])

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        product.save()
        return redirect('display')

    id = request.GET['id']
    product = Product.objects.get(id=id)

    return render(request, "display.html", {
        'pro': product,
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    })

