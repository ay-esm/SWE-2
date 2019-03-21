from django.shortcuts import render,redirect

# Create your views here.
from .forms import RepairForm

from .models import Repairtype,Repairpiece

def repair_piece_input(request):


    if request.method == 'POST':
        form = RepairForm(request.POST)

        if form.is_valid():
            save=form.save()

            cd=form.cleaned_data

            # if cd.get('type1'):
            #     obj= Repairtype()
            #     obj.pieceID=save.pk
            #     obj.typename= 'ashtatype1'
            #     obj.save()
            #
            # if cd.get('type2'):
            #     obj= Repairtype()
            #     obj.pieceID=save.pk
            #     obj.typename= 'ashtatype2'
            #     obj.save()
    else:
        form= RepairForm()

    context={'form':form}
    return render(request,'pieces/repair_piece_input.html',context)



def repair_item_View(request):
    repairobj= Repairpiece.objects.get(id=2)
    types= type


