# Generated by Django 4.0.1 on 2022-01-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_profile_companyname_alter_profile_priceperkg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pricePerKg',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
