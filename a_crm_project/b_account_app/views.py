from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dashboard(request):
    return render(request,"accounts/dashboard.html")

def products(request):
    return render(request,"accounts/products.html")

def customers(request):
    return render(request,"accounts/customer.html")
