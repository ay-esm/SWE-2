from django.shortcuts import render,redirect
from customer.models import Customer
from customer.forms import CustomerForm
# Create your views here.

def homeView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    else:
        context={}

        return render(request,'base.html',context)


def add_order_view(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            new_customer = Customer(name=request.POST['name'], phone=request.POST['phone'])
            new_customer.save()
            context = {}
            return render(request, 'addOrder.html', context)
    context = {}
    return render(request, 'addOrder.html', context)


def add_customer_view(request):
    form = CustomerForm()

    if request.is_ajax():
        context = {'backToOrder': 'no', 'form': form}
    else:
        context = {'form': form}
    return render(request, 'addCustomer.html', context)