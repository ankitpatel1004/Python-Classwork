from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from myapp.models import *
from myapp.serializers import *

# Create your views here.

class RestaurantAPI(APIView):
    def get(self,request):
        res = Restaurant.objects.all()
        ser = RestaurantSerializer(res,many=True)
        return Response({'data':ser.data},status=status.HTTP_200_OK)

    def post(self,request):
        ser = RestaurantSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)

class RestaurantAPIById(APIView):
    def get(self,request,id):
        res = Restaurant.objects.get(id=id)
        ser = RestaurantSerializer(res)
        return Response({'data':ser.data},status=status.HTTP_200_OK)

    def put(self,request,id):
        res = Restaurant.objects.get(id=id)
        ser = RestaurantSerializer(res,request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        res = Restaurant.objects.get(id=id)
        ser = RestaurantSerializer(res,request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            res = Restaurant.objects.get(id=id)
            res.delete()
            return Response({'message':'Restaurant Deleted Successfully!....'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message':'Restaurant Not Found!....' },status=status.HTTP_400_BAD_REQUEST)