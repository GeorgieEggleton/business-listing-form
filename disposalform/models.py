from django.db import models #imports the tools from django that are used to create the db models
from django.contrib.auth.models import User #I think this imports the tools from django to manage login / access to the db
from cloudinary.models import CloudinaryField #tools for inserting Cloudinary to the db
# from phonenumber_field.modelfields import PhoneNumberField


class Vendor(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on'] #order by asending order based on created on 

    def __str__(self):
        return f" {self.first_name}  {self.last_name}"




class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_address_line1 = models.CharField(max_length=200)
    business_address_line2 = models.CharField(max_length=200)
    business_county = models.CharField(max_length=50)
    business_postcode = models.CharField(max_length=10)
    ltd_compnay = models.BooleanField(default=False)
    ltd_compnay_name = models.CharField(max_length=200)
    tenure = models.CharField(max_length=200)
    takings = models.IntegerField()
    date_bought = models.DateTimeField()
    date_est = models.DateTimeField()
    menu = models.TextField()
    accommodation = models.BooleanField(default=False)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    equipment = models.TextField()
    deliveries = models.BooleanField(default=False)
    price = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="businesses") 
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']