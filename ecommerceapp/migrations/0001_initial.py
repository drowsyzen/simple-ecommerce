# Generated by Django 5.0.6 on 2024-07-07 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMstModel',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Active', 'active'), ('In-Active', 'inactive')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=1000, verbose_name='Product Code')),
                ('desc', models.CharField(max_length=1000, verbose_name='Product Desc')),
                ('price', models.CharField(max_length=1000, verbose_name='Price')),
                ('category', models.CharField(max_length=1000, verbose_name='Product Category')),
                ('quantity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Active', 'active'), ('In-Active', 'inactive')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_line', models.CharField(max_length=1000, verbose_name='Address line')),
                ('city', models.CharField(max_length=500, verbose_name='City')),
                ('state', models.CharField(max_length=500, verbose_name='State')),
                ('country', models.CharField(max_length=500, verbose_name='Country')),
                ('pincode', models.CharField(max_length=500, verbose_name='Pincode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentsModel',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Active', 'active'), ('In-Active', 'inactive')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_amount', models.IntegerField()),
                ('utr_no', models.CharField(max_length=1000, verbose_name='UTR')),
                ('payment_datetime', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Active', 'active'), ('In-Active', 'inactive')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerceapp.addressmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerceapp.paymentsmodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerceapp.productmstmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShoppingCartModel',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Active', 'active'), ('In-Active', 'inactive')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1)),
                ('is_ordered', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerceapp.productmstmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
