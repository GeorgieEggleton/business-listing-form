from django.shortcuts import render
from django.views import generic
from .models import Business


class BusinessList(generic.ListView):
    model = Business
    queryset = Business.order_by('price')
    template_name = 'index.html'
    
