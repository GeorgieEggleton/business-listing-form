from django.shortcuts import render
from django.views import generic
from .models import Business


class BusinessList(generic.ListView):
    model = Business
    queryset = Business.objects.order_by('created_on')
    template_name = 'index.html'
    
