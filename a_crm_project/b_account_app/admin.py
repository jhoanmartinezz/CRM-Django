from django.contrib import admin

# Register your models here.

#from .models import Customer# ===> new imports
from .models import * # ===> new import

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Tag)