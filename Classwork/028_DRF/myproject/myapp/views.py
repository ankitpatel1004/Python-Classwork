from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def create(request):
    return Response("POST API CALLING")

@api_view(['GET'])
def list(request):
    return Response("GET API CALLING")

@api_view(['PUT'])
def update(request):
    return Response("PUT API CALLING")

@api_view(['DELETE'])
def delete(request):
    return Response("DELETE API CALLING")
