from django.contrib import admin
from .models import Repair_order,Repair_item,Repair_option
# Register your models here.
admin.site.register(Repair_order,Repair_item,Repair_option)

