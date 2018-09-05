from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Relation)
class RelationAdmin(admin.ModelAdmin):

    search_fields =(
        'product1',
        'product2',
    )
    
    list_filter = (
        'product1',
        'product2',
        'count',
        'created_at'
    )

    list_display = (
        'product1',
        'product2',
        'count',
        'created_at'
    )