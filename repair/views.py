from django.shortcuts import render
from customer.forms import CustomerForm,CustomerForm2
from customer.models import Customer
from repair.forms import *
# Create your views here.


def add_order_view(request):
    if request.method == 'POST':
        form = CustomerForm2(request.POST)
        if form.is_valid():
            phone = request.POST.get("phone")
            cu = Customer.objects.filter(phone=phone)
            # print(cu.get("phone"))
            if(cu):
                form_item = Repair_item_From()
                context = {'go_to_items':1,'form':form,'form_item':form_item}
                return render(request, 'repair/addOrder.html', context)
            else:
                form_cu = CustomerForm()
                context={'form':form_cu}
                return render(request, 'repair/addCustomer.html', context)
            # new_customer = Customer(name=request.POST['name'], phone=request.POST['phone'])
            # new_customer.save()
            # context = {}
            # return render(request, 'repair/addOrder.html', context)
    else:
        form = CustomerForm()
        context = {'go_to_item':0,'form':form}
    return render(request, 'repair/addOrder.html', context)


def add_customer_view(request):
    form = CustomerForm()

    if request.is_ajax():
        context = {'backToOrder': 'no', 'form': form}
    else:
        context = {'form': form}
    return render(request, 'repair/addCustomer.html', context)

def add_items(request):
    form = Repair_item_From()