from django.shortcuts import render
from .filters import *

# Create your views here.
def index(request):
    context={}
    return render(request, 'repair/base.html', context)


def list_repairs(request):
    order_list = Repair_order.objects.all()
    order_filter = repair_filter(request.GET, queryset=order_list)
    context={'filter':order_filter}
    return render(request, 'list_repairs.html', context)
