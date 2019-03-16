from django.db import models

# Create your models here.
class repair(models.Model):
    price = models.TextField()
    name = models.TextField()
    phone = models.TextField()

