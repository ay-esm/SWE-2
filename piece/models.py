from django.db import models

# Create your models here.

class Repairtype(models.Model):
    typename= models.CharField(max_length=25)

    def __str__(self):
        return self.typename

class Repairpiece(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=4)
    types= models.ManyToManyField(Repairtype)


# class Repairtype(models.Model):
#     pieceID= models.IntegerField()
#     typename= models.CharField(max_length=2)


