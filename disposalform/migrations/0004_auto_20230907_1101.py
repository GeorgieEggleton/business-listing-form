# Generated by Django 3.2.20 on 2023-09-07 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('disposalform', '0003_auto_20230901_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='business',
            old_name='bathroms',
            new_name='bathrooms',
        ),
        migrations.AddField(
            model_name='vendor',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
