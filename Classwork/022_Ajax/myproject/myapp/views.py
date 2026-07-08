from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def test(request):
    q = request.GET['q']
    return HttpResponse(f"Ajax...{q}")

def search(request):
    q = request.GET['q']
    products = Product.objects.filter(name__startswith=q)
    data = "<ul>"
    for product in products:
        data+=f"<li>{product.name}</li>"
    data+="</ul>"
    # if q=='electric':
    #     data+="<ul><li>Fan</li><li>AC</li><li>Light</li></ul>"
    # elif q=='cloths':
    #      data+="<ul><li>Shirt</li><li>Jeans</li><li>Tshirt</li></ul>"
    # elif q=='sports':
    #      data+="<ul><li>Bat</li><li>Ball</li><li>Stump</li></ul>"
    # else :
    #     data+="No data found"
    return HttpResponse(data)

def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"data":list(countries.values())})

def states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(states.values())})

def cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(cities.values())})
    