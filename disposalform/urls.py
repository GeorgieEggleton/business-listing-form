from . import views
from django.urls import path

urlpatterns = [
    path('', views.BusinessList.as_view(), name='home'),
    path('<str:username>/', views.VendorInput.as_view(), name='vendor_input')
]