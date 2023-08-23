from django.db import models #imports the tools from django that are used to create the db models
from django.contrib.auth.models import User #I think this imports the tools from django to manage login / access to the db
from cloudinary.models import CloudinaryField #tools for inserting Cloudinary to the db


class Vendor(models.Model):
    title = models.Charfield(max_length=10)
    first_name = models.Charfield(max_length=50)
    last_name = models.Charfield(max_length=50)
    email = models.EmailField()
    address_line1 = models.Charfield(max_length=200)
    address_line2 = models.Charfield(max_length=200)
    county = models.Charfield(max_length=50)
    postcode = models.Charfield(max_length=10)
    phone_number = PhoneNumberField()
    mobile_number = PhoneNumberField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on'] #order by asending order based on created on 




class Business(models.Model):
    business_name = models.Charfield(max_length=100)
    business_address_line1 = models.Charfield(max_length=200)
    business_address_line2 = models.Charfield(max_length=200)
    business_county = models.Charfield(max_length=50)
    business_postcode = models.Charfield(max_length=10)
    ltd_compnay = models.BooleanField(default=False)
    ltd_compnay_name = models.Charfield(max_length=200)
    tenure = models.Charfield(max_length=200)
    takings = NumberField()
    date_bought = models.DateTimeField()
    date_est = models.DateTimeField()
    menu = models.TextField()
    accommodation = models.BooleanField(default=False)
    bedrooms = models.IntegerField()
    bathroms = models.IntegerField()
    equipment = models.TextField()
    deliveries = models.BooleanField(default=False)
    price = models.IntegerField()