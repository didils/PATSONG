from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields =(
        'product',
        'category',
        'code',
        'product_en',
    )

    list_display = (
        'product',
        'category',
        'code',
        'product_en',
    )