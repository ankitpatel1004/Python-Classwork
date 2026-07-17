from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
import requests

# Create your views here.

def index(request):
    return render(request,"index.html")

def mail_send(request):
    data = request.GET
    to = data.get('to')
    sub = data.get('subject')
    msg = data.get('message')
    send_mail(
        subject=sub,
        message=msg,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to],
        html_message="<h1>Hello Django</h1>",
        fail_silently=False
    )
    return render(request,"index.html",{"msg":"Email sent successfully"})

def mail_html(request):
    html_message = render_to_string(
        "demo.html",
    )

    email = EmailMultiAlternatives(
        subject = "Student Details",
        body = "Your email client does not support HTML.",
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = ["ankitpatel8085@gmail.com"]
    )

    email.attach_alternative(html_message, "text/html")
    email.send()
    return HttpResponse("HTML Email Sent!")

def mail_attach(request):
    email = EmailMessage(
        subject="Welcome",
        body="Please find the attached report.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["ankitpatel8085@gmail.com"],
    )
    # Attach a file from your project
    email.attach_file("media/shirt.jpg")
    email.send()
    return HttpResponse("Email with attachment sent successfully!")

def send_sms(request):

    url = "https://www.fast2sms.com/dev/bulkV2?route=q&message=hello&numbers=9173828868"

    headers = {
        "accept": "application/json",
        "Authorization": ""
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    return HttpResponse("SMS Sent")
