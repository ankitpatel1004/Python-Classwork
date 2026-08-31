from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializer import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework import status
import razorpay
import random

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class AddressViewSet(viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Return only addresses belonging to logged-in user.
        """
        return Address.objects.filter(
            user=self.request.user
        ).order_by("-is_default", "-created_at")
            
    def perform_create(self, serializer):
        """
        Automatically assign logged-in user.
        User does not need to send user ID.
        """
        serializer.save(
            user=self.request.user
        )
        
class CartViewSet(APIView):
    
    def get_cart(self,user):
        cart,created = Cart.objects.get_or_create(user=user)  
        return cart
    
    def get(self,request):
        # cart = Cart.objects.get(user=request.user)
        cart = self.get_cart(request.user)
        serializer = CartSerializer(cart)

        return Response(
                    {
                        "cart": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
    
    def post(self,request):
        data = request.data
        product = data['product']
        qty = data['qty']
        
        try:

            product = Product.objects.get(
                id=product,
                is_active=True
            )

        except Product.DoesNotExist:

            return Response(
                {
                    "error": "Product not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        cart = self.get_cart(request.user)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product= product,
            defaults={
                "quantity": qty
            }
        )
        
        if not created:
            new_quantity = (
                cart_item.quantity + qty
            )
        
            cart_item.quantity = new_quantity

            cart_item.save()
           
        serializer = CartSerializer(
            cart
        )

        return Response(
            {
                "message": "Product added to cart successfully.",
                "cart": serializer.data
            },
            status=status.HTTP_200_OK
        )
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment(request):
    amount = request.data['amount']
    id = "rzp_test_TDGqon3ZZeG3V9"
    secret="9f9QZ31p4RmGBTG52F33WXGJ"

    client = razorpay.Client(auth=(id,secret))

    data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    print(payment)
    return Response(payment)   
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def confirmorder(request):
    data = request.data
    transaction_id = data.get('transaction_id')
    payment_method = data.get('payment_method')
    amount = data.get("amount")
    
    user = request.user
    address = Address.objects.get(user=user,is_default=True)
    carts = Cart.objects.get(user=user)
    order_number = f"ORDER_{random.randint(0000,9999)}"
    total_amount = carts.total_amount
    
    order = Order.objects.create(user=user,address=address,order_number=order_number,total_amount=total_amount)
    
    items = carts.items.all()
    for i in items:  
        stotal = i.product.price*i.quantity
        OrderItem.objects.create(order=order,product=i.product,product_name=i.product.name,price=i.product.price,quantity=i.quantity,subtotal=stotal)
    
    carts.delete()
    
    Payment.objects.create(order=order,transaction_id=transaction_id,amount=amount,payment_method=payment_method)
    
    return Response("Success")

@api_view(['GET'])
def myorders(request):
    orders = Order.objects.get(user=request.user)
    ser = OrderSerializer(orders)
    return Response({"orders":ser.data})
    