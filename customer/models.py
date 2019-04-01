from django.db import models
from repair import models as rp
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_customer_phone(self,phone):
        queryset = ""
        return queryset
