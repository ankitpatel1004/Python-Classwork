from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def send_sms(request):

    url = "https://www.fast2sms.com/dev/bulkV2?route=q&message=hello&numbers=9898345421"

    headers = {
        "accept": "application/json",
        "Authorization": ""
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    return HttpResponse("SMS Sent")