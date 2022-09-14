from django.urls import path
from main.views import *

urlpatterns = [
    path('',contact,name='contact-page'),
]