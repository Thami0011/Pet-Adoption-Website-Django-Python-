from django.contrib import admin
from .models import Category,Item , Customer, Order , OrderItem

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)