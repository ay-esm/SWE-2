from django.shortcuts import render

# Create your views here.
from customer.models import Customer
from customer.forms import *

def search_for_customer_view(request):

    if (request.method == 'POST'):
        context = {}
    else:
        form = CustomerForm2()
        context = {'form': form}


    return render(request, 'addOrder.html', context)