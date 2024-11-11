from django.contrib import admin
from .models import Product, Warehouse, Group


admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Group)
