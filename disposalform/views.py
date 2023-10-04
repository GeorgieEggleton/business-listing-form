from django.shortcuts import render, get_object_or_404 
from django.views import generic, View 
from .models import Business, Vendor
from .forms import VendorForm, BusinessForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime


# Hope page view displayed on first load of the site or when logo cicked
class Home(View): 
    def get (self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.get_username() == 'admin':
                return redirect("/adminoverview")
            else: 
                return redirect("/overview") 
        else:
            return render(
                        request,
                        'index.html'
                    )
                
# Vendor input form. 
# Called when user logs in for the first time. 
# Only accessable if logged in. 
class VendorInput(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            try: 
                vendor = Vendor.objects.get(username = request.user.get_username())  
            except Vendor.DoesNotExist: 
                vendor = "" 

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
        
        vendor_form = VendorForm(data=request.POST)  
        if vendor_form.is_valid(): 
            vendor_form.instance.username = request.user.username
            vendor_form.instance.email = request.user.email
            vendor = vendor_form.save(commit=False)
            vendor.save()
            return redirect("/overview") 
        else:    
            return render(
                request,
                "vendor_input.html",
                {
                    "vendor" : vendor,
                    "vendor_form" : VendorForm(),
                    "error" : Error
                },
            ) 

# Business input form. 
# Called when user clickes to add a new Business 
# Only accessable if logged in. 
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
            business = business_form.save(commit=False)
            business.vendor = vendor
            business.save()
        
        return render(
           request,
           "business_input.html",
            {
                "business_form" : BusinessForm(data=request.POST),
                "error" : Error
            },
        ) 


# Loads the Business input form pre-populated with the current busines to be edited. 
# updates the information on the current busiess 
class BusinessUpdate(View):
    def get(self, request, id, *args, **kwargs):
       
        if request.user.is_authenticated: 
            SelectedBusiness = get_object_or_404(Business, id=id)
            if request.user.get_username() == SelectedBusiness.vendor.username:
                BForm = BusinessForm(instance=SelectedBusiness)
                
                return render(
                    request,
                    "business_input.html",
                    {
                    "business_form" : BForm,
                    "images" : SelectedBusiness.featured_image,
                    "business" : SelectedBusiness
                    },
                )
            else:
                return redirect("/accounts/login")     
        else:
            return redirect("/accounts/login")    

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated: 
            vendor = get_object_or_404(Vendor, username=request.user.get_username())
            existing_business = get_object_or_404(Business, id=id)

        business_form = BusinessForm(request.POST, request.FILES, instance=existing_business)  
        if business_form.is_valid(): 
            business = business_form.save(commit=False)
            business.save()
        return redirect("/overview") 


# Delete business - called when trash icon clicked on specific business
#Deletes the current business with unique ID only
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

# Overview shows the logged in users personal details and details of businesses linked to them
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
            vendor.email = request.user.email
            vendor.created_on = datetime.now()
            vendor.save()
        else: 
            Error = "we are not in the if statement"
        return redirect("overview") 
 
def custom_404(request, exception):
    return render(request, 'e404.html', status=404) 



# Admin overview - only accessable by the user logged in as admin
# Shows all busiesses and the linked vendor

class AdminOverview(View):
    def get (self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            if request.user.get_username() == "admin":  
                business_list = Business.objects.all()
                return render(
                    request,
                    'admin-overview.html',
                        {
                            "business_list" : business_list,
                        },
                ) 
            else: 
                return redirect("/accounts/login")  
        else: 
                return redirect("/accounts/login")         