# Generated by Django 3.2.16 on 2023-12-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastries',
            name='detail',
            field=models.TextField(max_length=500, verbose_name='Package Details'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Package Name'),
        ),
    ]
