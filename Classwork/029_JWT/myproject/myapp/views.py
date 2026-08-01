from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    return Response("User api calling")

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_admin(request):
    return Response("Admin api calling")

@api_view(['GET'])
@permission_classes([AllowAny])
def get_normal(request):
    return Response("Normal api calling")

