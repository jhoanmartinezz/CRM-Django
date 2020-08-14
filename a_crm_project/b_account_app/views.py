from django.shortcuts import render

from .models import *

# Create your views here.
from django.http import HttpResponse

def home(request):
    orders = Order.objects.all() #===> bring the orders
    customer = Customer.objects.all() #===> bring the customers
    total_customers = customer.count() #===> how many customers
    total_orders = orders.count() # ===> how many orders
    delivered = orders.filter(status='Delivered').count() # ===> hoy many orders delivered
    pending = orders.filter(status='Pending').count() # ===> how many pendings
    context = {"orders": orders, 
               "clientes": customer,
               "total_orders": total_orders,
               "total_customers": total_customers,
               "delivered": delivered,
               "pending": pending}
    return render(request,"accounts/dashboard.html", context)

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"accounts/products.html", context)

def customers(request):
    return render(request,"accounts/customer.html")
