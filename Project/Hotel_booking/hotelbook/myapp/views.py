from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request,"home.html")

def rooms(request):
    rooms = Room.objects.filter(available=True)
    return render(request,'rooms.html',{'rooms': rooms})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")

        return render(request,"login.html",{"err":"Invalid username or password"})

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmpassword")

        # Check passwords
        if password != confirm_password:
            return render(request, "register.html",{"err": "Password do not match"})

        # Check username
        if User.objects.filter(username=username).exists():
            return render(request, "register.html",{"err": "Username already exists"})

        # Create user
        User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,)
        return redirect("login")

    return render(request, "register.html")

def logout(request):
    auth_logout(request)
    return redirect("home")

def search_rooms(request):
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    guests = request.GET.get('guests')
    room_type = request.GET.get('room_type')

    # Start with available rooms
    rooms = Room.objects.filter(available=True)

    # ================= ROOM TYPE FILTER =================

    if room_type and room_type != "Any Room":
        rooms = rooms.filter(room_type=room_type)

    # ================= GUEST FILTER =================

    if guests:
        try:
            guests = int(guests)
            rooms = rooms.filter(capacity__gte=guests)
        except ValueError:
            guests = None

    # ================= DATE AVAILABILITY =================

    if check_in and check_out:

        try:
            check_in_date = datetime.strptime(
                check_in, "%Y-%m-%d"
            ).date()

            check_out_date = datetime.strptime(
                check_out, "%Y-%m-%d"
            ).date()

            # Find rooms already booked during these dates
            booked_room_ids = Booking.objects.filter(
                Q(status="Pending") | Q(status="Confirmed"),
                check_in__lt=check_out_date,
                check_out__gt=check_in_date
            ).values_list("room_id", flat=True)

            # Remove booked rooms from search results
            rooms = rooms.exclude(id__in=booked_room_ids)

        except ValueError:
            pass

    # ================= RETURN RESULTS =================

    return render(request, "rooms.html", {
        "rooms": rooms,
        "check_in": check_in,
        "check_out": check_out,
        "guests": guests,
        "room_type": room_type,
    })

@login_required(login_url='login')
def booking(request, room_id):

    room = get_object_or_404(Room, id=room_id)

    # Check room availability
    if not room.available:
        return render(request, "booking.html", {
            "room": room,
            "err": "This room is currently unavailable."
        })

    if request.method == "POST":

        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        guests = request.POST.get("guests")

        # ================= DATE VALIDATION =================

        try:
            check_in_date = datetime.strptime(
                check_in,
                "%Y-%m-%d"
            ).date()

            check_out_date = datetime.strptime(
                check_out,
                "%Y-%m-%d"
            ).date()

        except (ValueError, TypeError):

            return render(request, "booking.html", {
                "room": room,
                "err": "Please enter valid dates."
            })

        if check_out_date <= check_in_date:

            return render(request, "booking.html", {
                "room": room,
                "err": "Check-out date must be after check-in date."
            })

        # ================= GUEST VALIDATION =================

        try:
            guests = int(guests)

        except (ValueError, TypeError):

            return render(request, "booking.html", {
                "room": room,
                "err": "Please enter a valid number of guests."
            })

        if guests < 1:

            return render(request, "booking.html", {
                "room": room,
                "err": "At least one guest is required."
            })

        if guests > room.capacity:

            return render(request, "booking.html", {
                "room": room,
                "err": f"This room can accommodate only {room.capacity} guests."
            })

        # ================= BOOKING AVAILABILITY =================

        overlapping_booking = Booking.objects.filter(
            room=room
        ).filter(
            Q(status="Pending") | Q(status="Confirmed")
        ).filter(
            check_in__lt=check_out_date,
            check_out__gt=check_in_date
        ).exists()

        if overlapping_booking:

            return render(request, "booking.html", {
                "room": room,
                "err": "Sorry, this room is already booked for these dates."
            })

        # ================= PRICE =================

        nights = (check_out_date - check_in_date).days

        total_price = room.price * nights

        # ================= CREATE BOOKING =================

        booking_obj = Booking.objects.create(
            user=request.user,
            room=room,
            check_in=check_in_date,
            check_out=check_out_date,
            guests=guests,
            total_price=total_price,
            status="Pending"
        )

        # ================= RAZORPAY =================

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        # Razorpay uses paise
        amount = int(total_price * 100)

        razorpay_order = client.order.create({
            "amount": amount,
            "currency": "INR",
            "receipt": f"booking_{booking_obj.id}",
            "payment_capture": 1
        })

        # Save Razorpay order ID
        booking_obj.razorpay_order_id = razorpay_order["id"]
        booking_obj.save()

        # ================= PAYMENT PAGE =================

        return render(request, "payment.html", {

            "booking": booking_obj,

            "room": room,

            "razorpay_order_id":
                razorpay_order["id"],

            "razorpay_key":
                settings.RAZORPAY_KEY_ID,

            "amount":
                amount,
        })

    return render(request, "booking.html", {
        "room": room
    })

@csrf_exempt
@login_required(login_url='login')
def payment_success(request):

    if request.method != "POST":
        return redirect("rooms")

    payment_id = request.POST.get(
        "razorpay_payment_id"
    )

    order_id = request.POST.get(
        "razorpay_order_id"
    )

    signature = request.POST.get(
        "razorpay_signature"
    )

    if not payment_id or not order_id or not signature:

        return render(request, "payment_failed.html", {
            "error": "Payment information is incomplete."
        })

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    try:

        # Verify Razorpay signature
        client.utility.verify_payment_signature({

            "razorpay_order_id": order_id,

            "razorpay_payment_id": payment_id,

            "razorpay_signature": signature

        })

        # Find booking
        booking_obj = get_object_or_404(
            Booking,
            razorpay_order_id=order_id,
            user=request.user
        )

        # Save payment information
        booking_obj.razorpay_payment_id = payment_id

        # Confirm booking
        booking_obj.status = "Confirmed"

        booking_obj.save()

        return redirect("booking_success")

    except razorpay.errors.SignatureVerificationError:

        return render(request, "payment_failed.html", {
            "error": "Payment verification failed."
        })

def booking_success(request):
    return render(request,"booking_success.html")
