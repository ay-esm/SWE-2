from django.shortcuts import render, redirect, reverse
from .filters import *
from customer.forms import CustomerForm, CustomerForm2
from customer.models import Customer
from repair.forms import *
from repair.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from urllib.parse import urlencode


@login_required
def add_order_view(request):
    #if method is post (
    if request.method == 'POST':
        form = CustomerForm2(request.POST)
        context={}
        if form.is_valid():
            phone = request.POST.get("phone")
            #print(phone)
            cu = None
            if Customer.objects.filter(phone=phone):
                cu = Customer.objects.get(phone=phone)
            # print(cu[0]['name'])
            if cu:
                order_obj = Repair_order(customer_id=cu)
                order_obj.save()
                base_url = reverse('repair:AddI')  # 1 /addItem/
                query_string = urlencode({'phone': request.POST['phone'], 'order': order_obj.id})  # 2 phone=011
                url = '{}?{}'.format(base_url, query_string)  # concatenate to this form  /addItem/?phone=011&order=1
                return redirect(url)
            else:
                url = reverse('repair:AddC')
                return redirect(url, request)

    else:
        form = CustomerForm()
        context = {'go_to_item': 0, 'form': form}
    return render(request, 'repair/addOrder.html', context)


@login_required
def add_customer_view(request):
    form = CustomerForm()
    if request.method == "POST":
        new_customer = Customer(name=request.POST['name'], phone=request.POST['phone'])
        new_customer.save()
        order_obj = Repair_order(customer_id=new_customer)
        order_obj.save()
        base_url = reverse('repair:AddI')  # 1 /addItem/
        query_string = urlencode({'phone': request.POST['phone'], 'order': order_obj.id})  # 2 phone=011
        url = '{}?{}'.format(base_url, query_string)  # concatenate to this form  /addItem/?phone=011&order=1

        return redirect(url)
    else:
        context = {'form': form}
    return render(request, 'repair/addCustomer.html', context)


@login_required
def add_items(request):
    context={}
# coming from order page attached with PHONE
    if 'phone' in request.GET:
        phone = request.GET["phone"]
        cu = Customer.objects.filter(phone=phone).values('name')
# coming from order page attached with PHONE with valid phone attached to a customer
        if cu:
            name = cu[0]['name']
            form = CustomerForm(initial={'name': name, 'phone': phone})
            context = {'form': form}
            Dataform = Repair_order_From()
            context['date'] = Dataform
            if request.method == 'GET':
                print(context)
                    # On first render print the formsets

                formset = repair_form_set(initial=[{'type1': '-', 'type2': '-', 'type3': '-', 'option': '-', 'price': 0,
                                                    'summary': ''}])

                context['formset'] = formset

                return render(request, 'repair/AddItem.html', context)
            elif request.method == 'POST':
                # submitted N form for N items
                request_params = request.POST
                formset = repair_form_set(request_params)
                # print(type(formset[0]))  type: repair item form
                #print("HI")

                if formset.is_valid():
                    #print("HI")
                    for form in formset:
                        print("valid")
                        if form.is_valid():
                            # if form.cleaned_data.get('type1') and form.cleaned_data.get('type2') and form.cleaned_data.get('type3')  and form.cleaned_data.get('option') and form.cleaned_data('summary') and form.cleaned_data('price'):
                            type1 = form.cleaned_data.get('type1')
                            type2 = form.cleaned_data.get('type2')
                            type3 = form.cleaned_data.get('type3')
                            option = form.cleaned_data.get('option')

                            summary = form.cleaned_data.get('summary')
                            price = form.cleaned_data.get('price')
                            order_pk = request.GET['order']
                            order = Repair_order.objects.get(pk=order_pk)
                            current_order_price = order.total_price
                            order.total_price=current_order_price+price
                            order.reminder=current_order_price+price
                            order.save()
                            item = Repair_item(type1=type1, type2=type2, type3=type3,repair_order_id=order,
                                               summary=summary, price=price)
                            item.save()
                            option_i = Repair_option(option_name=option,)
                            option_i.save()
                            option_i.items_option.add(item)

                url = reverse('repair:listrepairs')
                return redirect(url)
        else:
            if request.method == 'GET':
                formset = repair_form_set(initial=[{'type1': '-', 'type2': '-', 'type3': '-', 'option': '-', 'price': 0,
                                                    'summary': ''}])
                context['formset'] = formset
                return render(request, 'repair/AddItem.html', context)
            elif request.method == 'POST':
                #print("hi")
                formset = repair_form_set(request.POST)
                if formset.is_valid():
                    #print("hi")
                    for form in formset:
                        type1 = form.cleaned_data.get('type1')
                        type2 = form.cleaned_data.get('type2')
                        type3 = form.cleaned_data.get('type3')
                        option = form.cleaned_data.get('option')
                        summary = form.cleaned_data('summary')
                        price = form.cleaned_data('price')
                    url = reverse('repair:listrepairs')
                    return redirect(url)
    return render(request, 'repair/AddItem.html', context)


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