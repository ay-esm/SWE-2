from django.db import models

# Create your models here.
class Repair_order(models.Model):
    phone=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    payed=models.DecimalField(decimal_places=2,max_digits=1000)
    reminder=models.DecimalField(decimal_places=2,max_digits=1000)
    total_price=models.DecimalField(decimal_places=2,max_digits=1000)
    current_date=models.DateField()
    estimate_date=models.DateField()

class Repair_item(models.Model):
    type1=models.CharField(max_length=15)
    type2=models.CharField(max_length=15)
    type3=models.CharField(max_length=15)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    order_id=models.IntegerField()

class Repair_option(models.Model):
    option_name = models.CharField(max_length=50)