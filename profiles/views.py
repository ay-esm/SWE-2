from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import messages
from .forms import UserForm,UserUpdateForm
from .models import EmpUser

# Create your views here.

def register_view(request):
    role=str(request.user.role)
    if  role != "Admin":
        print(role)
        return redirect('error-access')
    else:
        form = UserForm(request.POST or None)

        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'{username} تم عمل حساب بأسم ')
            return redirect('register')

        context={'form':form}

        return render(request, 'profileforms/register.html', context)

def login_view(request):
    return render(request, 'profileforms/login.html', {})

def error_access_view(request):
    return render(request, 'accesserror.html', {})


def list_all_accounts_view(request):
    role = str(request.user.role)
    if role != "Admin":
        print(role)
        return redirect('error-access')
    else:
        queryset = EmpUser.objects.all()
        context = {
            "accounts": queryset
        }

        return render(request, 'profileforms/list_accounts.html', context)

def profile_view(request,username):
    role = str(request.user.role)
    if role != "Admin":
        print(role)
        return redirect('error-access')
    else:
        obj = get_object_or_404(EmpUser,username=username)
        context = {
            "account": obj
        }

        return render(request, 'profileforms/profile.html', context)

def edit_profile_view(request,username):
    role = str(request.user.role)
    if role != "Admin":
        print(role)
        return redirect('error-access')
    else:
        obj = get_object_or_404(EmpUser, username=username)
        form = UserUpdateForm(request.POST or None , instance=obj)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}  تم تعديل حساب  ')
            print("ashta")
            return redirect(f"/profile/{username}/edit")

        context = {'form': form}
    return render(request, 'profileforms/update_account.html', context)


# def delete_account_view(request, username):
#     obj= get_object_or_404(EmpUser, username=username)
#     print(request.method)
#     obj.delete()
#     redirect("/list/acc")
#     context={"object": obj}
#
#     return render(request, 'profileforms/delete_account.html',context)

def delete_account_view(request, username):
    role = str(request.user.role)
    if role != "Admin":
        print(role)
        return redirect('error-access')
    else:
        obj= get_object_or_404(EmpUser, username=username)
        if request.method == 'POST' :
            print(request.method)
            form = UserForm(request.POST , instance=obj)
            obj.delete()
            return redirect("/listacc")
        else:
            form = UserForm(instance=obj)
            print("didnt deleted")
        context={"object": obj,  "form":form}

        return render(request, 'profileforms/delete_account.html',context)
