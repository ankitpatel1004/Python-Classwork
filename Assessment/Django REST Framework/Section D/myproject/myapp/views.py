from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.serializers import *

# Create your views here.

class PlaceOrderAPIView(APIView):
    def get(self,request):
        order = Order.objects.all()
        ser = OrderSerializer(order,many=True)
        return Response({'data':ser.data},status=status.HTTP_200_OK)

    def post(self,request):
        ser = OrderSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':ser.data},status=status.HTTP_400_BAD_REQUEST)