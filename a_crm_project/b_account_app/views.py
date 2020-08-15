from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from b_account_app.forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

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

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders_customer = customer.order_set.all()
    order_count = orders_customer.count()
    myFilter = OrderFilter(request.GET, queryset=orders_customer)
    orders_customer = myFilter.qs
    context = {'customer':customer, 
               "orders_customer":orders_customer,
               "order_count":order_count,
               "myFilter":myFilter}
    return render(request,"accounts/customer.html", context)

def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request,"accounts/order_form.html", context)

def updateOrder(request, pk):
    data = Order.objects.get(id=pk)
    form = OrderForm(instance=data)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request,"accounts/order_form.html", context)

def deleteOrder(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("/")
    context = {'item':item}
    return render(request,"accounts/delete_order.html", context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account created successfully for {}".format(user))
            return redirect("login")
    context = {'form':form}
    return render(request,"accounts/register.html",context)

def loginPage(request):
    context = {}
    return render(request,"accounts/login.html",context)
