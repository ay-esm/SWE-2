from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):

    return render(request, 'repair/base.html', context)
