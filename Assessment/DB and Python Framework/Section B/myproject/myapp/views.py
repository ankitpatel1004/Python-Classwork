from django.shortcuts import render, redirect
from .forms import UserProfileForms
from .models import UserProfile


def create_profile(request):

    if request.method == "POST":
        form = UserProfileForms(request.POST)

        if form.is_valid():
            UserProfile.objects.create(
                username=form.cleaned_data["username"],
                age=form.cleaned_data["age"],
                is_public=form.cleaned_data["is_public"]
            )
            return redirect("profile_list")

    else:
        form = UserProfileForms()
    return render(
        request,
        "create_profile.html",
        {"form": form}
    )

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(
        request,
        "profile_list.html",
        {"profiles": profiles}
    )
    