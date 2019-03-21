from django.db import models
from customer.models import Customer
# Create your models here.

class Repair_order(models.Model):
    phone=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    payed=models.DecimalField(decimal_places=2,max_digits=1000)
    reminder=models.DecimalField(decimal_places=2,max_digits=1000)
    total_price=models.DecimalField(decimal_places=2,max_digits=1000)
    current_date=models.DateField()
    estimate_date=models.DateField()
    customer_id = models.ForeignKey('customer.Customer',on_delete=models.CASCADE,default=1)
    state_to_office = models.BooleanField(default=False)
    state_to_store = models.BooleanField(default=False)
    state_to_customer = models.BooleanField(default=False)

class Repair_item(models.Model):
    type1=models.CharField(max_length=15)
    type2=models.CharField(max_length=15)
    type3=models.CharField(max_length=15)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    repair_order_id = models.ForeignKey('Repair_order', on_delete=models.CASCADE,default=1)
    state_finish= models.BooleanField(default=False)

class Repair_option(models.Model):
    option_name = models.CharField(max_length=50)
    items_option = models.ManyToManyField(Repair_item)
