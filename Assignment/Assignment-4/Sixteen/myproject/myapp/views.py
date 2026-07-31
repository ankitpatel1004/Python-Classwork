from django.shortcuts import render
import razorpay
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def payment(request):
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_TDGqon3ZZeG3V9", "9f9QZ31p4RmGBTG52F33WXGJ"))

    DATA = {
        "amount": amt*100,
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }
    payment=client.order.create(data=DATA)
    print(payment)
    return JsonResponse(payment)