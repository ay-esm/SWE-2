from .models import *
from django import forms
from django.core.validators import RegexValidator


class CustomerForm(forms.Form):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

    name = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control ta-r',
                                   'placeholder': 'الاسم',
                               }))
    phone = forms.CharField(required=True,
                            validators=[numeric],
                            widget=forms.TextInput(attrs={
                                'class': 'form-control ta-r',
                                'placeholder': 'رقم الهاتف',
                            }))
