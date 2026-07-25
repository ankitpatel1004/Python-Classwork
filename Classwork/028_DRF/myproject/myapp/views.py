from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *

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

@api_view(['GET'])
def list_student(request):
    students = Student.objects.all()
    ser = StudentSerializer(students,many=True)
    return Response({"data":ser.data})

@api_view(['POST'])
def create_student(request):
    ser = StudentSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data})

@api_view(['DELETE'])
def delete_student(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return Response("Student deleted")

@api_view(['PUT'])
def update_student(request,id):
    students = Student.objects.get(id=id)
    ser = StudentSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data})    