from django.urls import path
from ecom.views import *

urlpatterns = [
    path("categories",CategoryAPI.as_view()),
    path("categories/<id>",CategoryAPIbyId.as_view()),
    path("products",ProductAPI.as_view()),
    path("products/<id>",ProductAPIbyID.as_view()),
    path("products/category/<id>",product_category,name="product_category")
]