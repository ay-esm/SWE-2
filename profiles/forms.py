from .models import *
from django import forms


class UserForm(forms.Form):
    username    = forms.CharField(max_length=20,label='اسم المستخدم')
    password1   = forms.CharField(label='كلمة السر', widget=forms.PasswordInput)
    password2   = forms.CharField(label='كرر كلمة السر', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['username','password1','password2']


class ProfileForm(forms.Form):


    name = forms.CharField(max_length=150,label='الاسم كامل')
    address = forms.CharField(max_length=100,label="العنوان" )
    phone = forms.CharField(max_length=11, label='رقم الموبيل')
    national_ID = forms.CharField(max_length=14, label='الرقم القومي')
    edu = forms.CharField(max_length=50, label='المؤهل الدراسي')

    class Meta:
        model = Profile
        widgets ={'user_type': forms.Select}
        user_type = forms.ModelChoiceField(queryset=Usertype.objects.all(),label='نوع المستخدم', widget=forms.Select)

        fields = ['name','address','phone','national_ID','edu','user_type']