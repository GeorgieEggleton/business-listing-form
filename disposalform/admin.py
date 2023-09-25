from django.contrib import admin
from .models import Vendor, Business


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_name', 'business_postcode', 'vendor')