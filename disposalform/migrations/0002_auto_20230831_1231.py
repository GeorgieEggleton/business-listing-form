# Generated by Django 3.2.20 on 2023-08-31 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disposalform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='disposalform.vendor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]