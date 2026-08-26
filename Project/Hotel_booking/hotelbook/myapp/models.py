from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):

    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Executive', 'Executive'),
        ('Deluxe', 'Deluxe'),
        ('Suite', 'Suite'),
        ('Luxury', 'Luxury')
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    capacity = models.PositiveIntegerField(default=1)

    image = models.ImageField(
        upload_to='rooms/',
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5.0
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Booking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    check_in = models.DateField()
    check_out = models.DateField()

    guests = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"
