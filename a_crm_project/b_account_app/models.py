from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #name in panel amdin
    def __str__(self):
        return self.name

#tabla que une product y orders
class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)
    #name in panel admin
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'indoor'), 
        ('Out door', 'outdoor')
    )
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True,choices=CATEGORY)
    description = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #Foreign key
    tag = models.ManyToManyField(Tag)
    #name in panel admin
    def __str__(self):
        return self.name
    
#tabla que une customer y product
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'out for delivery'),
        ('Delivered', 'delivered'),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
    #Foreing key
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    #name in panel admin
    def __str__(self):
        return self.product.name
    