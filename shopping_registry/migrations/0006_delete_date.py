# Generated by Django 4.0 on 2022-02-02 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_registry', '0005_alter_purchase_date_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
    ]
