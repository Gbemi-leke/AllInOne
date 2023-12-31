# Generated by Django 3.2.16 on 2023-12-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_img', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Blog Image')),
                ('blog_title', models.CharField(max_length=100, verbose_name='Blog Title')),
                ('blog_description', models.TextField(verbose_name='Description')),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Image')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Other Images')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Other Images')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Other Images')),
                ('product_detail', models.TextField(max_length=100, verbose_name='Package Details')),
                ('vendor_brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('price', models.CharField(max_length=20, verbose_name='Price')),
                ('size', models.CharField(max_length=20, verbose_name='Size')),
                ('available_product', models.CharField(max_length=20, verbose_name='Available product')),
                ('delivery_fee', models.CharField(max_length=20, verbose_name='Delivery Fee')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Fashion',
            },
        ),
        migrations.CreateModel(
            name='Gadgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Image')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Other Images')),
                ('detail', models.TextField(max_length=500, verbose_name='Gadget Details')),
                ('vendor_brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('price', models.CharField(max_length=20, verbose_name='Price')),
                ('colour', models.CharField(max_length=20, verbose_name='Colour')),
                ('available_product', models.CharField(max_length=20, verbose_name='No. of available Gadgets')),
                ('delivery_fee', models.CharField(max_length=20, verbose_name='Delivery Fee')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Gadgets',
            },
        ),
        migrations.CreateModel(
            name='Pastries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Image')),
                ('detail', models.TextField(max_length=100, verbose_name='Package Details')),
                ('vendor_brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('price', models.CharField(max_length=20, verbose_name='Price')),
                ('delivery_fee', models.CharField(max_length=20, verbose_name='Delivery Fee')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Pastries',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Image')),
                ('title', models.CharField(max_length=100, verbose_name='Package Name')),
                ('brand', models.CharField(max_length=100, verbose_name='Vendor Brand')),
                ('price', models.CharField(max_length=20, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('delivery', models.CharField(max_length=20, verbose_name='Delivery Fee')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant',
            },
        ),
        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
