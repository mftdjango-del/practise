from django.contrib import admin
from .models import ProductModel, Category, Color
# Register your models here.


admin.site.register(ProductModel)
admin.site.register(Category)
admin.site.register(Color)