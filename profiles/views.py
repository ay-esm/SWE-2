from django.shortcuts import render
from .forms import UserForm,ProfileForm

# Create your views here.

def register_view(request):
    user_form = UserForm(request.POST)
    profile_form   = ProfileForm(request.POST)

    if user_form.is_valid() and profile_form.is_valid():
        u = user_form.save()
        p=profile_form.save(commit= False)
        p.user=u
        p.save()

    context={'u_form':user_form, 'p_form':profile_form}

    return render(request, 'profileforms/register.html', context)