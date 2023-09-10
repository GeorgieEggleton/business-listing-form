from .models import Vendor 
from django import forms 


class VendorForm(forms.ModelForm):
    
    
    class Meta:
        model = Vendor
        fields = (
        'title',
        'email',
        'title',
        'first_name',
        'last_name',
        'address_line1',
        'address_line2',
        'county',
        'postcode',
        'phone_number',
        'mobile_number',
        )