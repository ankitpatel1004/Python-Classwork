from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from ecom.models import *
from ecom.serializer import *
from rest_framework import status

# Create your views here.

class CategoryAPI(APIView):

    def get(self,request):
        categories = Category.objects.all()
        ser = CategorySerializer(categories,many=True)
        return Response({"data":ser.data},status=status.HTTP_200_OK)

    def post(self,request):
        ser = CategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)

class CategoryAPIbyId(APIView):
    
    def get(self,request,id):
        category = Category.objects.get(id=id)
        ser = CategorySerializer(category)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response({"message":"category delete"},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
             return Response({"message":"category not found"},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        category = Category.objects.get(id=id)
        ser = CategorySerializer(category,request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)

class ProductAPI(APIView):
    
    def get(self,request):
        products = Product.objects.all()
        ser = ProductSerializer(products,many=True)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
        
    def post(self,request):
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)
            
class ProductAPIbyID(APIView):

    def get(self,request,id):
        product = Product.objects.get(id=id)
        ser = ProductSerializer(product)
        return Response({"dat":ser.data},status=status.HTTP_200_OK)

    def put(self,request,id):
        product = Product.objects.get(id=id)
        ser = ProductSerializer(product,request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"message":"Product deleted"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_category(request,id):
    products = Product.objects.filter(category_id=id)
    ser = ProductSerializer(products,many=True)
    return Response({"data":ser.data})
