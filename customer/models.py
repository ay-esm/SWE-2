from django.db import models
from repair import models as rp
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return "id :" + str(self.id)+" name :" + self.name
