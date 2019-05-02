from django.db import models
from django.contrib.auth.models import User,Group,AbstractBaseUser,AbstractUser
# Create your models here.
# class Usertype(models.Model):
#     usertype    = models.CharField(max_length= 20)
#
#     def __str__(self):
#         return self.usertype


class EmpUser(AbstractUser):
    #user        = models.OneToOneField(User,on_delete=models.CASCADE)
    name        = models.CharField(max_length = 150)
    address     = models.CharField(max_length = 100)
    phone       = models.CharField(max_length = 11)
    national_ID = models.CharField(max_length = 14)
    edu         = models.CharField(max_length = 50)
    REQUIRED_FIELDS = ['email','name','address','phone','national_ID','edu']
    #user_type   = models.ForeignKey(Usertype,on_delete=models.CASCADE)
    role        = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)



