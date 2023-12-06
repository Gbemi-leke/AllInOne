# Generated by Django 3.2.16 on 2023-11-17 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20231117_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='newuser',
            name='account_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('vendor', 'Vendor'), ('user', 'User')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
