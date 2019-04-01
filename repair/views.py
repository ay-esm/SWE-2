from django.shortcuts import render,redirect
from .filters import *
from customer.forms import CustomerForm,CustomerForm2
from customer.models import Customer
from repair.forms import *
# Create your views here.


def add_order_view(request):


    if not request.user.is_authenticated:
        return redirect('login')
    else:


        if request.method == 'POST':
            form = CustomerForm2(request.POST)
            context={}
            if form.is_valid():
                phone = request.POST.get("phone")
                #print(phone)
                cu = Customer.objects.filter(phone=phone).values('name')
                # print(cu[0]['name'])
                if(cu):
                    name = cu[0]['name']
                    form = CustomerForm(initial={'name':name,'phone':phone})

                    context = {'go_to_items':1,'form':form}

                    return add_items(request,context)
                else:
                    form_cu = CustomerForm()
                    context={'form':form_cu}
                    return render(request, 'repair/addCustomer.html', context)

        else:
            form = CustomerForm()
            context = {'go_to_item':0,'form':form}
        return render(request, 'repair/addOrder.html', context)


def add_customer_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:


        form = CustomerForm()
        if request.method == "POST":
            new_customer = Customer(name=request.POST['name'], phone=request.POST['phone'])
            new_customer.save()
            context = {'backToOrder': 'no', 'form': form}
            return render(request, 'repair/addItem.html', context)
        else:
            context = {'form': form}
        return render(request, 'repair/addCustomer.html', context)


def add_items(request,context):
    if not request.user.is_authenticated:
        return redirect('login')
    else:

        form = Repair_item_From()
        if request.method == 'GET':
            formset = repair_form_set(request.GET or None)
        context['form_item'] = form
        return render(request,'repair/AddItem.html',context)


def list_repairs(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:

        order_list = Repair_order.objects.all()
        order_filter = repair_filter(request.GET, queryset=order_list)
        context={'filter':order_filter}
        return render(request, 'repair/list_repairs.html', context)

