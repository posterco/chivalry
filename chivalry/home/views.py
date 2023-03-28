from django.shortcuts import render , HttpResponseRedirect
from accounts.models import *
from django.contrib import messages
import calendar
from calendar import HTMLCalendar
from datetime import datetime



def landing_page(request):
    return render(request , 'landing.html')

def goals(request):
    context  = {'category' : Category.objects.filter() , 'goals': Goals.objects.filter()}
    return render(request,'goals.html' , context)

def add_goal(request , uid):
    goal= Goals.objects.filter(uid=uid)
    user = request.user
    
    goal_user = UserGoals.objects.get_or_create(user=user)
    print(goal[0])
    print(goal_user[0])

    goal_user[0].goals.add(goal[0])

    messages.success(request , 'Added Successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home(request , year=datetime.now().year,month=datetime.now().strftime('%B')):
    user = request.user
    
    goal_user = UserGoals.objects.filter(user=user)

    goals = goal_user[0].goals.all()

    
    context  = {'category' : Category.objects.filter() , 'goals' : goals}
    return render(request,'home.html' , context)