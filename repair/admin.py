from django.contrib import admin
from .models import Repair_item,Repair_option,Repair_order
# Register your models here.
admin.site.register(Repair_order)
admin.site.register(Repair_option)
admin.site.register(Repair_item)