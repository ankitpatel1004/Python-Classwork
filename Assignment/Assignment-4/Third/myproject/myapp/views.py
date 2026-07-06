from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,"base.html")

def explore(request):
    return render(request,"explore.html")

def profile(request):
    return render(request,"profile.html")