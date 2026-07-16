from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request,"index.html")

def mail_send(request):
    data = request.GET
    to = data.get('to')
    sub = data.get('subject')
    messages = data.get('message')
    send_mail(
        subject=sub,
        message=messages,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to],
        html_message="<h1>Hello Django</h1>",
        fail_silently=False
    )
    return render(request,"index.html",{"msg":"Email sent successfully"})
