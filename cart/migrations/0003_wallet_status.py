# Generated by Django 4.1.4 on 2023-05-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
