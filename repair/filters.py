from django import forms
from .models import *
import django_filters


class repair_filter(django_filters.FilterSet):
    STATUS_CHOICES = (
        ('True', 'تم'),
        ('False', 'لم يتم'),
    )
    customer_id = django_filters.ModelChoiceFilter(queryset=Customer.objects.all(),
                                                   widget=forms.Select(
                                                        attrs={
                                                            'class': 'form-control form-control-sm',
                                                            'id': 'material-select',
                                                            'name': 'material-select',
                                                            'size': '1'}
                                                   )
                                                   )
    state_to_office = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    state_to_store = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    state_to_customer = django_filters.ChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        model = Repair_order
        fields = ['customer_id', 'total_price', 'payed', 'state_to_office', 'state_to_store', 'state_to_customer']
