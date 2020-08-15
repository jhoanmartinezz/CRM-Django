from django.contrib import admin
from django.urls import path

 #===> new import
from b_account_app import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create-order"),
    path('update_order/<str:pk>', views.updateOrder, name="update-order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete-order"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
]