from django.db import models

# Create your models here.
class order(models.Model):
    phone=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    payed=models.DecimalField(decimal_places=2,max_digits=1000)
    reminder=models.DecimalField(decimal_places=2,max_digits=1000)
    total_price=models.DecimalField(decimal_places=2,max_digits=1000)
    current_date=models.DateField()
    estimate_date=models.DateField()

class omar(models.Model):
    phone = models.TextField()