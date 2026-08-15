from rest_framework import serializers
from myapp.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','price','is_available','category']

    def validate_price(self, value): 
        if value <= 0: raise serializers.ValidationError( "Price must be greater than 0." ) 
        return value

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category'] = CategorySerializer(instance.category).data
        return resp