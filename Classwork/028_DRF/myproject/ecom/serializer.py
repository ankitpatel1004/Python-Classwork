from rest_framework import serializers
from ecom.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
            model=Product
            fields='__all__'
            # fields=['id','name']
            # exclude=['name']
            depth = 1

    def validate(self, attrs):
        if attrs['qty']<1:
            raise serializers.ValidationError({"qty":"Quantity must be atleast 1"})
        return attrs