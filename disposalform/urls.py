from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('overview/', views.Overview.as_view(), name='overview'),
    path('vendorinput/', views.VendorInput.as_view(), name='vendorinput'),
    path('businessinput/', views.BusinessInput.as_view(), name='businessinput'),
    path('deletebusiness/<int:id>', views.DeleteBusiness.as_view(), name='deletebusiness'),
    path('businessupdate/<int:id>', views.BusinessUpdate.as_view(), name='businessupdate'),
    
]