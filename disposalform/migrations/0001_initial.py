# Generated by Django 3.2.20 on 2023-08-31 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_address_line1', models.CharField(max_length=200)),
                ('business_address_line2', models.CharField(max_length=200)),
                ('business_county', models.CharField(max_length=50)),
                ('business_postcode', models.CharField(max_length=10)),
                ('ltd_compnay', models.BooleanField(default=False)),
                ('ltd_compnay_name', models.CharField(max_length=200)),
                ('tenure', models.CharField(max_length=200)),
                ('takings', models.IntegerField()),
                ('date_bought', models.DateTimeField()),
                ('date_est', models.DateTimeField()),
                ('menu', models.TextField()),
                ('accommodation', models.BooleanField(default=False)),
                ('bedrooms', models.IntegerField()),
                ('bathroms', models.IntegerField()),
                ('equipment', models.TextField()),
                ('deliveries', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
