from django.shortcuts import render,redirect
from .filters import *
from customer.forms import CustomerForm,CustomerForm2
from customer.models import Customer
from repair.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def add_order_view(request):
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
                context ={'form':form}
                return redirect('addItem/'+'?'+'phone='+phone)
            else:
                return redirect('add/',request)

    else:
        form = CustomerForm()
        context = {'go_to_item':0,'form':form}
    return render(request, 'repair/addOrder.html', context)


@login_required
def add_customer_view(request):
    form = CustomerForm()
    if request.method == "POST":
        new_customer = Customer(name=request.POST['name'], phone=request.POST['phone'])
        new_customer.save()
        context = {'form': form}
        return redirect('addItem/'+'?'+'phone='+phone)
    else:
        context = {'form': form}
    return render(request, 'repair/addCustomer.html', context)


@login_required
def add_items(request):
    context={}
    if 'phone' in request.GET:
        phone = request.GET["phone"]
        cu = Customer.objects.filter(phone=phone).values('name')
        if(cu):
            name = cu[0]['name']
            form = CustomerForm(initial={'name': name, 'phone': phone})
            context = {'form': form}
            if request.method == 'GET':
                formset = repair_form_set(initial=[{'type1':'-','type2':'-','type3':'-','option':'-','price':0,'summary':''}])
                context['formset'] = formset
                return render(request,'repair/AddItem.html',context)
            elif request.method=='POST':
                formset = repair_form_set()
                context['formset'] = formset
            if formset.is_valid():
                for form in formset:
                    type1 = form.cleaned_data.get('type1')
                    type2 = form.cleaned_data.get('type2')
                    type3 = form.cleaned_data.get('type3')
                    option = form.cleaned_data.get('option')
                    summary = form.cleaned_data('summary')
                    price = form.cleaned_data('price')

                return redirect('repair/list_repairs.html')
        else:
            if request.method == 'GET':
                formset = repair_form_set(initial=[{'type1':'-','type2':'-','type3':'-','option':'-','price':0,'summary':''}])
                context['formset'] = formset
                return render(request,'repair/AddItem.html',context)
            elif request.method=='POST':
                formset = repair_form_set()
                context['formset'] = formset
            if formset.is_valid():
                for form in formset:
                    type1 = form.cleaned_data.get('type1')
                    type2 = form.cleaned_data.get('type2')
                    type3 = form.cleaned_data.get('type3')
                    option = form.cleaned_data.get('option')
                    summary = form.cleaned_data('summary')
                    price = form.cleaned_data('price')
                return redirect('repair/list_repairs.html')
    return render(request,'repair/AddItem.html',context)


@login_required
def list_repairs(request):
    order_list = Repair_order.objects.all()
    order_filter = repair_filter(request.GET, queryset=order_list)
    context={'filter':order_filter}
    return render(request, 'repair/list_repairs.html', context)




# def create_book_normal(request):
#     template_name = 'store/create_normal.html'
#     heading_message = 'Formset Demo'
#     if request.method == 'GET':
#         formset = BookFormset(request.GET or None)
#     elif request.method == 'POST':
#         formset = BookFormset(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 # extract name from each form and save
#                 name = form.cleaned_data.get('name')
#                 # save book instance
#                 if name:
#                     Book(name=name).save()
#             # once all books are saved, redirect to book list view
#             return redirect('book_list')
#     return render(request, template_name, {
#         'formset': formset,
#         'heading': heading_message,
# })
#https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0?fbclid=IwAR239lUIbWG7suikvZrNlyp_T71xKDy_t1ThVCyE_YzaF6xeCHIEBQNgkvQ