# Generated by Django 3.2.20 on 2023-09-07 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disposalform', '0004_auto_20230907_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='username',
        ),
    ]
