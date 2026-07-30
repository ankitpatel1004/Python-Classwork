from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        artist = data.get('artist')
        duration = data.get('duration')

        playlist.objects.create(title=title,artist=artist,duration=duration)
        return HttpResponse("Song Added Successfully!")

def display_data(request):
    playlists = playlist.objects.all()
    return JsonResponse({'data':list(playlists.values())})

def delete_song(request):
    id = request.GET['id']
    play = playlist.objects.get(id=id)
    play.delete()
    return HttpResponse("Song Deleted Successfully!")

def retrive_data(request):
    id = request.GET['id']
    play = playlist.objects.filter(id=id)
    return JsonResponse({'play':list(play.values())})

def update_data(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        title = data.get('title')
        artist = data.get('artist')
        duration = data.get('duration')

        playlists = playlist.objects.get(id=id)
        playlists.title = title
        playlists.artist = artist
        playlists.duration = duration
        playlists.save()
        return HttpResponse("Song Updated Successfully!")