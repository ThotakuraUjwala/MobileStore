# Generated by Django 5.1.3 on 2025-02-04 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_laptops'),
    ]

    operations = [
        migrations.CreateModel(
            name='lapBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(upload_to='brand_logos/')),
            ],
        ),
        migrations.AlterField(
            model_name='laptops',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.lapbrand'),
        ),
    ]
