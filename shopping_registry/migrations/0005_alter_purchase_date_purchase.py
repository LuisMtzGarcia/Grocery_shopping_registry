# Generated by Django 4.0 on 2022-02-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_registry', '0004_category_owner_date_owner_product_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='date_purchase',
        ),
        migrations.AddField(
            model_name='purchase',
            name='date_purchase',
            field=models.DateField(),
        ),
    ]
