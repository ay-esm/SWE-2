from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm

# Create your views here.

def register_view(request):
    form = UserForm(request.POST or None)


    if form.is_valid():
        form.save()
        username= form.cleaned_data.get('username')
        messages.success(request, f'{username}تم عمل حساب بأسم ')
        return redirect('register')

    context={'form':form}

    return render(request, 'profileforms/register.html', context)

def login_view(request):
    return render(request, 'profileforms/login.html', {})