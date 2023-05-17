# Generated by Django 4.1.4 on 2023-05-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review_rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150),
        ),
    ]
