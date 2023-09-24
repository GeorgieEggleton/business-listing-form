from django.shortcuts import render, get_object_or_404 
from django.views import generic, View 
from .models import Business, Vendor
from .forms import VendorForm, BusinessForm
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
        
        #Take the information typed by the user in the form and create an instance of the class "VendorForm" from the forms.py file.  
        #This will be called "vendorform" 
        vendor_form = VendorForm(data=request.POST)  
        if vendor_form.is_valid(): #if crispy forms thinks that the user input is "valid" i.e. if the date is in in the wrong format, or all the fields are not complete
            Error = "we are in the if statement!!!"
            vendor_form.instance.username = request.user.username
            vendor_form.instance.email = request.user.email
            vendor = vendor_form.save(commit=False)
            vendor.save()
        else:
            #vender_form = VendorForm() # if form invalid return empty form    
            Error = "we are not in the if statement"
        return render(
            request,
            "vendor_input.html",
            {
                "vendor" : vendor,
                "vendor_form" : VendorForm(),
                "error" : Error
            },
        ) 


class BusinessInput(View):
    def get(self, request, *args, **kwargs):
       #if request.user.is_authenticated: # check to see if the user is logged in
        return render(
            request,
            "business_input.html",
            {
                "business_form" : BusinessForm()
            },
    )


        

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            vendor = get_object_or_404(Vendor, username=request.user.get_username())
            #try:  
            #   vendor = Vendor.objects.get(username = request.user.get_username())  
            #except Vendor.DoesNotExist: 
             #   vendor = "Vendor Does Not Exist" 
        
        business_form = BusinessForm(request.POST, request.FILES)  
        if business_form.is_valid(): 
            Error = "we are in the if statement!!!"
            business = business_form.save(commit=False)
            business.vendor = vendor
            business.save()
        else: 
            Error = "we are not in the if statement"
        return render(
           request,
           "business_input.html",
            {
                "business_form" : BusinessForm(data=request.POST),
                "error" : Error
            },
        ) 



