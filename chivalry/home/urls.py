from django.urls import path
from .views import *

urlpatterns = [
    path('' , landing_page , name='landing_page'),
    path('goals' , goals , name="goals"),
    path('home' , home , name="home"),
    path('add_goal/<uid>/' , add_goal , name="add_goal"),
]