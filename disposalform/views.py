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

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated: # check to see if the user is logged in
            try:  # This will check if the "Vendor.objects.get" command does not throw an error
                vendor = Vendor.objects.get(username = request.user.get_username())  # this will look for the variable username in the "Vendor" table 
            except Vendor.DoesNotExist: # if the record does not exist in the "Vendor" database return text below 
                vendor = "Vendor Does Not Exist" #text assigned to variable vendor if the record "username" doesn not exist 

        

        return render(
            request,
            "vendor_input.html",
            {
                "vendor" : vendor,
                "vendor_form" : VendorForm()
            },
    )

    def post(self, request, *args, **kwargs):
        
        if request.user.is_authenticated: # check to see if the user is logged in
            try:  # This will check if the "Vendor.objects.get" command does not throw an error
                vendor = Vendor.objects.get(username = request.user.get_username())  # this will look for the variable username in the "Vendor" table 
            except Vendor.DoesNotExist: # if the record does not exist in the "Vendor" database return text below 
                vendor = "Vendor Does Not Exist" #text assigned to variable vendor if the record "username" doesn not exist 

        
 
       #  post = get_object_or_404(queryset, slug=slug)
      
        
        vendor_form = VendorForm(data=request.POST)
        vendor_form.instance.email = "ddddd"
        if vendor_form.is_valid():
            
            vendor_form.instance.username = request.user.username
            VendorUpdate = vendor_form.save(commit=False)
            VendorUpdate.post = post
            comment.save()
        else:
            VendorForm = CommentForm() # if form invalid return empty form    

        return render(
            request,
            "vendor_input.html",
            {
                "vendor" : vendor,
                "vendor_form" : VendorForm()
            },
        ) 

 



