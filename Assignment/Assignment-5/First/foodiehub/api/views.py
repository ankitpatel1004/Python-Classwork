from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def hello_spotify(request):
    return JsonResponse({'message':'Hello, Spotify Fans!'})