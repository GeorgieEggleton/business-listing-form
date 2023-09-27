from django.shortcuts import render, get_object_or_404 
from django.views import generic, View 
from .models import Business, Vendor
from .forms import VendorForm, BusinessForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime


class Home(View): 
    def get (self, request, *args, **kwargs):
        return render(
                    request,
                    'index.html'
                )
                

class BusinessList(generic.ListView):
    model = Business
    queryset = Business.objects.order_by('created_on')
    template_name = 'index.html'

    def delete(request, id):
        member = Member.objects.get(id=id)
        member.delete()
        return HttpResponseRedirect(reverse('index'))



class VendorInput(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: # check to see if the user is logged in
            try:  # This will check if the "Vendor.objects.get" command does not throw an error
                vendor = Vendor.objects.get(username = request.user.get_username())  # this will look for the variable username in the "Vendor" table 
            except Vendor.DoesNotExist: # if the record does not exist in the "Vendor" database return text below 
                vendor = "" #text assigned to variable vendor if the record "username" doesn not exist 

            return render(
                request,
                "vendor_input.html",
                {
                    "vendor" : vendor,
                    "vendor_form" : VendorForm()
                },
            )    
        else: 
            return redirect("/accounts/login")         

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            try:  
                vendor = Vendor.objects.get(username = request.user.get_username())  
            except Vendor.DoesNotExist: 
                vendor = "Vendor Does Not Exist" 
        
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
        if request.user.is_authenticated: 
                return render(
                    request,
                    "business_input.html",
                    {
                    "business_form" : BusinessForm()
                    },
                )    
        else:
            return redirect("/accounts/login")    
        
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            vendor = get_object_or_404(Vendor, username=request.user.get_username())
            
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




class BusinessUpdate(View):
    def get(self, request, id, *args, **kwargs):
       
        if request.user.is_authenticated: 
            SelectedBusiness = get_object_or_404(Business, id=id)
            if request.user.get_username() == SelectedBusiness.vendor.username:
                return render(
                    request,
                    "business_input.html",
                    {
                    "business_form" : BusinessForm(instance=SelectedBusiness)
                    },
                )
            else:
                return redirect("/accounts/login")     
        else:
            return redirect("/accounts/login")    



        

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated: 
            vendor = get_object_or_404(Vendor, username=request.user.get_username())
          
        
        business_form = BusinessForm(request.POST, request.FILES)  
        if business_form.is_valid(): 
            Error = "we are in the if statement!!!"
            business = business_form.save(commit=False)
            business.vendor = vendor
            business.id = id
            business.created_on = datetime.now()
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


class DeleteBusiness(View):
    
    def post(self, request, id):
        
        SelectedBuisness = get_object_or_404(Business, id=id) 
        if request.user.is_authenticated: 
            if request.user.get_username() == SelectedBuisness.vendor.username:
                SelectedBuisness.delete() 
                ConfirmDelete = "Deleted"     

        return render(
           request,
           'delete-business.html',
            {
                
                "business" : SelectedBuisness,
                "confirmdelete" : ConfirmDelete
            },
        ) 



class Overview(View):
    def get (self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            try:  
                vendor = Vendor.objects.get(username = request.user.get_username()) 
                business_list = Business.objects.all()
                return render(
                    request,
                    'overview.html',
                        {
                            "business_list" : business_list,
                            "vendor" : vendor
                        },
                )
            except Vendor.DoesNotExist: 
                return redirect("vendorinput") 
        else: 
            return redirect("/accounts/login")     


class VendorUpdate(View):
    def get(self, request, id, *args, **kwargs):
       
        if request.user.is_authenticated: 
            SelectedVendor = get_object_or_404(Vendor, id=id)
            if request.user.get_username() == SelectedVendor.username:
                return render(
                    request,
                    "vendor_input.html",
                    {
                    "vendor_form" : VendorForm(instance=SelectedVendor)
                    },
                )
            else:
                return redirect("/accounts/login")     
        else:
            return redirect("/accounts/login")    
        
    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated: 
            vendor = get_object_or_404(Vendor, username=request.user.get_username())
        
        vendor_form = VendorForm(request.POST, request.FILES)  
        if vendor_form.is_valid(): 
            Error = "we are in the if statement!!!"
            vendor = vendor_form.save(commit=False)
            vendor.id = id
            vendor.username = request.user.get_username()
            vendor.email = vendor.email
            vendor.created_on = datetime.now()
            vendor.save()
        else: 
            Error = "we are not in the if statement"
        return redirect("overview") 
 