from .models import Vendor, Business
from django import forms 
from cloudinary.forms import CloudinaryFileField


class VendorForm(forms.ModelForm):
    
    class Meta:
        model = Vendor
        fields = (
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

class BusinessForm(forms.ModelForm):
    date_bought = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label = "What date did you take ownership of the business?"
    )
    date_est = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label = "Approximately when was the site established as a Fish & Chip shop?"
    )
    
    class Meta:
        model = Business

        fields = (
            'business_name',
            'business_address_line1',
            'business_address_line2',
            'business_county',
            'business_postcode',
            'ltd_company',
            'ltd_company_name',
            'tenure',
            'takings',
            'deliveries',
            'menu',
            'date_bought',
            'date_est',
            'equipment',
            'accommodation',
            'bedrooms',
            'bathrooms',
            'price',
            'featured_image',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['business_name'].label = "What is the trading name of the business?"
        self.fields['business_address_line1'].label = "Address line 1"
        self.fields['business_address_line2'].label = "Address line 2"
        self.fields['business_county'].label = "County"
        self.fields['business_postcode'].label = "Post Code"
        self.fields['ltd_company'].label = "Is the business run as a Limited Company?"
        self.fields['ltd_company_name'].label = "What is the name of the Ltd Company?"
        self.fields['tenure'].label = "Is the business freehold or leasehold?"
        self.fields['takings'].label = "What is the average weekly takings of the business?"
        self.fields['deliveries'].label = "Do you offer home deliveries?"
        self.fields['menu'].label = "Menu summary"
        self.fields['equipment'].label = "Equipment Summary"
        self.fields['accommodation'].label = "Is there any accomodation included with the business?"
        self.fields['bedrooms'].label = "Number of bedrooms?"
        self.fields['bathrooms'].label = "Number of bathrooms?"
        self.fields['price'].label = "Agreed asking price"
        self.fields['featured_image'].label = "Photo"
        

    