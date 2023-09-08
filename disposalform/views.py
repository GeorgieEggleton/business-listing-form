from django.shortcuts import render, get_object_or_404 
from django.views import generic, View 
from .models import Business, Vendor
from .forms import VendorForm
from django.shortcuts import render
from django.contrib.auth.models import User


class BusinessList(generic.ListView):
    model = Business
    queryset = Business.objects.order_by('created_on')
    template_name = 'index.html'


class VendorInput(View):

    def get(self, request, username, *args, **kwargs):
        
        
        vendor = Vendor.objects.get(username="SparkyDoo")

        return render(
            request,
            "vendor_input.html",
            {
                "vendor" : vendor,
                "VendorForm" : VendorForm()
            },
    )

 



