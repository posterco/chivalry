from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.models import *
import random

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            messages.warning(request , 'Account not found')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect('/goals')

        else:
            messages.warning(request , 'Invalid Email Id or Password')
            return HttpResponseRedirect(request.path_info)
        
    return render(request , 'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request , 'Account with this Email already exists')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name=first_name , last_name=last_name , email=email , username=email)
        user_obj.set_password(password)
        user_obj.save()
        return render(request , 'accounts/login.html')
    return render(request , 'accounts/register.html')
