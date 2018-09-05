from django.db import models
 
class Relation(models.Model):
    
    product1 = models.CharField(max_length=80, null=True, blank=True)
    product2 = models.CharField(max_length=80, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '지정상품1: {} vs 지정상품2: {}: 카운트: {}'.format(self.product1, self.product2, self.count)
    
    class Meta:
        ordering =['-created_at']