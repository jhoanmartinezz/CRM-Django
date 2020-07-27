from django.contrib import admin
from django.urls import path

from . import views #===> new import


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customers/', views.customers, name="customers"),
]