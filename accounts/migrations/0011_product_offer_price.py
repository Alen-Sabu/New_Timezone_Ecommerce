# Generated by Django 4.1.4 on 2023-04-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_offer_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
