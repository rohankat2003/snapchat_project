from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Invoice(models.Model):
    invoice_date = models.DateField(null=True,blank=True)
    invoice_number=models.CharField(max_length=10,null=True,blank=True)
    customer_name=models.CharField(max_length=100,null=True,blank=True)
    due_date=models.DateField(null=True,blank=True)
    product_name=models.CharField(max_length=100,null=True,blank=True)
    qty=models.CharField(max_length=10,null=True,blank=True)
    rate=models.CharField(max_length=10,null=True,blank=True)
    total=models.CharField(max_length=10,null=True,blank=True)
    user=models.ForeignKey(User,related_name="create_invoice",on_delete=models.DO_NOTHING)

    def _str_(self):
        return self.name