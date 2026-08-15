from rest_framework import serializers
from myapp.models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id","customer_name","item","quantity"]

    def validated_quantity(self,value):
        if not isinstance(value,int) or isinstance(value,bool):
            raise serializers.ValidationError(
                "Quantity must be a positive integer."
            )

        if value<=0:
            raise serializers.ValidationError("Quantity must be a positive intger.")
        return value
        