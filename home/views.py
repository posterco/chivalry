from django.shortcuts import render
from accounts.models import *



def landing_page(request):
    return render(request , 'landing.html')

def goals(request):
    context  = {'category' : Category.objects.filter() , 'goals': Goals.objects.filter()}
    return render(request,'goals.html' , context)
