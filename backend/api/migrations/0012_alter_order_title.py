# Generated by Django 4.0.1 on 2022-01-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_order_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]