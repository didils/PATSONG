from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Case)
class CaseAdmin(admin.ModelAdmin):

    search_fields =(
        'trademark_title',
        'owner',
        'request_date',
        'payment_date',
    )
    
    list_filter = (
        'trademark_title',
        'owner',
        'request_date',
        'payment_date',
    )

    list_display = (
        'trademark_title',
        'trademark_image',
        'owner',
        'request_date',
        'payment_date',
    )
