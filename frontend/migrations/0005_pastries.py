# Generated by Django 3.2.16 on 2023-11-25 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0004_rename_vendor_brand_fashion_vendor_brand'),
    ]

    operations = [
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pastries',
            },
        ),
    ]
