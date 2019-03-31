from .models import *
from django import forms
from django.core.validators import RegexValidator


class CustomerForm(forms.Form):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

    name = forms.CharField(required=True,
                           label="الاسم",
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control ta-r',
                               }))
    phone = forms.CharField(required=True,
                            validators=[numeric],
                            label="رقم الموبايل",
                            widget=forms.TextInput(attrs={
                                'class': 'form-control ta-r',
                            }))
class CustomerForm2(forms.Form):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
    phone = forms.CharField(required=True,
                            validators=[numeric],
                            widget=forms.TextInput(attrs={
                                'class': 'form-control ta-r',
                                'placeholder': 'رقم الهاتف',
                            }))
