from django.db import models

class Product(models.Model):    

    product = models.CharField(max_length=255, null=True, blank=True)
    category = models.IntegerField(null=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    product_en = models.CharField(max_length=255, null=True, blank=True)
        
    def __str__(self):
        return '{}({})'.format(self.product, self.product_en)