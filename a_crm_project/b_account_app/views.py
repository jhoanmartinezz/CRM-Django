from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from b_account_app.forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            messages.success(request, "Account created successfully for {}".format(username))
            return redirect("login")
    context = {'form':form}
    return render(request,"accounts/register.html",context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password incorrect')
    context = {}
    return render(request,"accounts/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("login")

def userPage(request):
	context = {}
	return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"accounts/products.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request,"accounts/order_form.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("/")
    context = {'item':item}
    return render(request,"accounts/delete_order.html", context)

