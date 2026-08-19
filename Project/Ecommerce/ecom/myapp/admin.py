from django.contrib import admin

# Register your models here.

from .models import (
    User,
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
# ADDRESS ADMIN
# ============================================================

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "full_name",
        "phone",
        "city",
        "state",
        "pincode",
        "country",
        "is_default",
    )

    list_filter = (
        "country",
        "state",
        "city",
        "is_default",
    )

    search_fields = (
        "user__username",
        "user__email",
        "full_name",
        "phone",
        "city",
        "pincode",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# CATEGORY ADMIN
# ============================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# PRODUCT ADMIN
# ============================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "price",
        "quantity",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
        "category__name",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "price",
        "quantity",
        "is_active",
    )


# ============================================================
# CART ADMIN
# ============================================================

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
        "total_amount",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# CART ITEM ADMIN
# ============================================================

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
        "subtotal",
        "created_at",
    )

    list_filter = (
        "product__category",
    )

    search_fields = (
        "cart__user__username",
        "cart__user__email",
        "product__name",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# ORDER ADMIN
# ============================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order_number",
        "user",
        "total_amount",
        "status",
        "address",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "order_number",
        "user__username",
        "user__email",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "status",
    )


# ============================================================
# ORDER ITEM ADMIN
# ============================================================

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order",
        "product",
        "product_name",
        "price",
        "quantity",
        "subtotal",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "order__order_number",
        "product_name",
        "product__name",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# PAYMENT ADMIN
# ============================================================

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order",
        "transaction_id",
        "amount",
        "payment_method",
        "status",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "payment_method",
        "status",
        "created_at",
    )

    search_fields = (
        "transaction_id",
        "order__order_number",
        "order__user__username",
        "order__user__email",
    )

    ordering = (
        "-created_at",
    )