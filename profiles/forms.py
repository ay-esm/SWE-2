from .models import *
from django import forms


class UserForm(forms.Form):
    username    = forms.CharField(max_length=20, label='اسم المستخدم', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    password1   = forms.CharField(label='كلمة السر', widget=forms.PasswordInput(
                                attrs={
                                       'class': 'form-control ta-r',
                                    }))
    password2   = forms.CharField(label='كرر كلمة السر', widget=forms.PasswordInput(
                                attrs={
                                       'class': 'form-control ta-r',
                                    }))

    class Meta:
        model= User
        fields=['username','password1','password2']


class ProfileForm(forms.Form):


    name = forms.CharField(max_length=150,label='الاسم كامل', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    address = forms.CharField(max_length=100,label="العنوان" , widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    phone = forms.CharField(max_length=11, label='رقم الموبيل', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    national_ID = forms.CharField(max_length=14, label='الرقم القومي', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    edu = forms.CharField(max_length=50, label='المؤهل الدراسي', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))

    class Meta:
        model = Profile
        widgets ={'user_type': forms.Select}
        user_type = forms.ModelChoiceField(queryset=Usertype.objects.all(),label='نوع المستخدم', widget=forms.Select(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))

        fields = ['name','address','phone','national_ID','edu','user_type']