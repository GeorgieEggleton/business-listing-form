from . import views
from django.urls import path

urlpatterns = [
    path('', views.BusinessList.as_view(), name='home'),
    path('vendorinput/', views.VendorInput.as_view(), name='vendor_input'),
    path('businessinput/', views.BusinessInput.as_view(), name='business_input')
    
]