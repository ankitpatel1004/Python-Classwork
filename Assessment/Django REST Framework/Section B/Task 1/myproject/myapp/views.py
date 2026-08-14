from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from myapp.models import *
from myapp.serializers import *

# Create your views here.

class CategoryAPI(APIView):
    def get(self,request):
        cat = Category.objects.all()
        ser = CategorySerializer(cat,many=True)
        return Response({'data':ser.data},status=status.HTTP_200_OK)

    def post(self,request):
        ser = CategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)
            