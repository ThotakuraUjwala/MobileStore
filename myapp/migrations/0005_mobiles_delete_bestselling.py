# Generated by Django 5.1.3 on 2025-01-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_slides'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('origprice', models.IntegerField()),
                ('ram', models.CharField(max_length=30, null=True)),
                ('rom', models.CharField(max_length=30, null=True)),
                ('camera', models.CharField(max_length=100, null=True)),
                ('battery', models.CharField(max_length=100, null=True)),
                ('overview', models.TextField(max_length=3000, null=True)),
                ('is_bestselling', models.BooleanField(default=False, null=True)),
                ('is_deals', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='bestselling',
        ),
    ]
