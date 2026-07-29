from django.shortcuts import render,redirect
from myapp.forms import *
from myapp.models import *
from django.http import HttpResponse
import csv

# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request,"profile_list.html",{'profiles':profiles})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm()
    return render(request,"profile_form.html",{'form':form})

def export_profiles(request):
    response = HttpResponse(content_type="text/csv")
    response['content-Disposition'] = 'attchment; filename="profiles.csv'
    with open('profiles.csv','w',newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Username",
            "Age",
            "Email",
            "Public"
        ])

        profiles = Profile.objects.all()

        for profile in profiles:
            writer.writerow([
                profile.username,
                profile.age,
                profile.email,
                profile.is_public
            ])

    with open("profiles.csv","r") as file:
        response.write(file.read())
    return response
    