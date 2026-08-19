from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Address,
    Category,
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Payment,
)


# ============================================================
# USER SERIALIZER
# ============================================================

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]

        read_only_fields = ["id"]
        
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        user.save()
        return user
# ============================================================
# ADDRESS SERIALIZER
# ============================================================

class AddressSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Address

        fields = [
            "id",
            "user",
            "full_name",
            "phone",
            "address_line",
            "city",
            "state",
            "country",
            "pincode",
            "is_default",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]


# ============================================================
# CATEGORY SERIALIZER
# ============================================================

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = [
            "id",
            "name",
            "description",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


# ============================================================
# PRODUCT SERIALIZER
# ============================================================

class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Product

        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "description",
            "price",
            "quantity",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "category_name",
            "created_at",
            "updated_at",
        ]


# ============================================================
# CART ITEM SERIALIZER
# ============================================================

class CartItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_price = serializers.DecimalField(
        source="product.price",
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    subtotal = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = CartItem

        fields = [
            "id",
            "cart",
            "product",
            "product_name",
            "product_price",
            "quantity",
            "subtotal",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "product_name",
            "product_price",
            "subtotal",
            "created_at",
            "updated_at",
        ]


# ============================================================
# CART SERIALIZER
# ============================================================

class CartSerializer(serializers.ModelSerializer):

    user = UserSerializer(
        read_only=True
    )

    items = CartItemSerializer(
        many=True,
        read_only=True
    )

    total_amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Cart

        fields = [
            "id",
            "user",
            "items",
            "total_amount",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "items",
            "total_amount",
            "created_at",
            "updated_at",
        ]


# ============================================================
# ORDER ITEM SERIALIZER
# ============================================================

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem

        fields = [
            "id",
            "order",
            "product",
            "product_name",
            "price",
            "quantity",
            "subtotal",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "product_name",
            "price",
            "subtotal",
            "created_at",
        ]


# ============================================================
# ORDER SERIALIZER
# ============================================================

class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(
        read_only=True
    )

    address = AddressSerializer(
        read_only=True
    )

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order

        fields = [
            "id",
            "user",
            "address",
            "order_number",
            "total_amount",
            "status",
            "items",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "order_number",
            "total_amount",
            "items",
            "created_at",
            "updated_at",
        ]


# ============================================================
# PAYMENT SERIALIZER
# ============================================================

class PaymentSerializer(serializers.ModelSerializer):

    order_number = serializers.CharField(
        source="order.order_number",
        read_only=True
    )

    class Meta:
        model = Payment

        fields = [
            "id",
            "order",
            "order_number",
            "transaction_id",
            "amount",
            "payment_method",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "order_number",
            "transaction_id",
            "amount",
            "status",
            "created_at",
            "updated_at",
        ]