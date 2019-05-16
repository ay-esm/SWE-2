from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class UserForm(forms.ModelForm):
    username    = forms.CharField(max_length=20, label='اسم المستخدم', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    password   = forms.CharField(label='كلمة السر', widget=forms.PasswordInput(
                                attrs={
                                       'class': 'form-control ta-r',
                                    }))
    confirm_password   = forms.CharField(label='كرر كلمة السر', widget=forms.PasswordInput(
                                attrs={
                                       'class': 'form-control ta-r',
                                    }))
    name = forms.CharField(max_length=150, label='الاسم كامل', widget=forms.TextInput(
        attrs={
            'class': 'form-control ta-r',
        }))
    address = forms.CharField(max_length=100, label="العنوان", widget=forms.TextInput(
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
    role = forms.ModelChoiceField(queryset=Group.objects.all(), label='نوع المستخدم', widget=forms.Select(
        attrs={
            'class': 'form-control tr-r'})
                                  )

    class Meta:
        model= EmpUser
        fields=['username','password','confirm_password','name','address','phone','national_ID','edu','role']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")

        if len(password) < 6:
            raise forms.ValidationError("the password must be more than 5 characters")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")

        return cleaned_data




    # def clean_confirm_password(self):
    #     #cleaned_data = super(UserForm, self).clean()
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data["confirm_password"]
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError("password and confirm_password does not match")
    #     return password
    #
    # def clean_password(self):
    #     passw= self.cleaned_data['password']
    #
    #     if len(passw) < 6:
    #         raise forms.ValidationError("the password must be more than 5 characters")
    #     return passw


# class UserUpdateForm(UserChangeForm):
#     class Meta:
#         model = EmpUser
#         fields = ['username', 'name']


class UserUpdateForm(UserChangeForm):
    username    = forms.CharField(max_length=20, label='اسم المستخدم', widget=forms.TextInput(
                                 attrs={
                                       'class': 'form-control ta-r',
                                    }))
    # password   = forms.CharField(label='كلمة السر', widget=forms.PasswordInput(
    #                             attrs={
    #                                    'class': 'form-control ta-r',
    #                                 }))
    # confirm_password   = forms.CharField(label='كرر كلمة السر', widget=forms.PasswordInput(
    #                             attrs={
    #                                    'class': 'form-control ta-r',
    #                                 }))
    name = forms.CharField(max_length=150, label='الاسم كامل', widget=forms.TextInput(
        attrs={
            'class': 'form-control ta-r',
        }))
    address = forms.CharField(max_length=100, label="العنوان", widget=forms.TextInput(
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
    role = forms.ModelChoiceField(queryset=Group.objects.all(), label='نوع المستخدم', widget=forms.Select(
        attrs={
            'class': 'form-control tr-r'})
                                  )

    password = None
    class Meta:
        model= EmpUser
        fields=['username','name','address','phone','national_ID','edu','role']
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserUpdateForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    # def clean(self):
    #     cleaned_data = super(UserUpdateForm, self).clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get("confirm_password")
    #     print(confirm_password)
    #     if len(password) < 6:
    #         raise forms.ValidationError("the password must be more than 5 characters")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError("password and confirm_password does not match")
    #
    #     return cleaned_data





