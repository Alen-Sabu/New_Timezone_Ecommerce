# Generated by Django 4.1.4 on 2023-05-11 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=200, null=True)),
                ('pincode', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, region=None)),
                ('email', models.EmailField(max_length=150)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('min_price', models.FloatField(default=0)),
                ('discount', models.FloatField()),
                ('valid_from', models.DateTimeField(null=True)),
                ('valid_to', models.DateTimeField(null=True)),
                ('active', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('total_price', models.FloatField(null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Return Requested', 'Return Requested'), ('Return Approved', 'Return Approved')], default='Pending', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Return', 'Return'), ('ReturnApproved', 'ReturnApproved')], default='Pending', max_length=150)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cancelled', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.billingaddress')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.coupon')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(through='cart.OrderedItems', to='accounts.product')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.FloatField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product')),
                ('wishlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=200, null=True)),
                ('pincode', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, region=None)),
                ('email', models.EmailField(max_length=150)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.ordereditems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(max_length=100)),
                ('total_amount', models.FloatField()),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.payment'),
        ),
        migrations.AddField(
            model_name='orders',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.shippingaddress'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.FloatField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product')),
            ],
        ),
        migrations.AddField(
            model_name='ordereditems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.orders'),
        ),
        migrations.AddField(
            model_name='ordereditems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.product'),
        ),
    ]
