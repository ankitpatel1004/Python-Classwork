from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from myapp.serializers import *

# Create your views here.

@api_view(['POST'])
def get_reg(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({'message':'Registration Successfully'})
    else:
        return Response({'errors':ser.errors})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    return Response({'message':'User API Calling'})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_admin(request):
    return Response({'message':'Admin API Calling'})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_normal(request):
    return Response({'message':'Normal API Calling'})
    