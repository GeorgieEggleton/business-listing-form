from .models import Vendor 
from django import forms 


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('title', 'first_name', 'last_name',)