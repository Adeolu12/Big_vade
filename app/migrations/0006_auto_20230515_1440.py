# Generated by Django 3.2.18 on 2023-05-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cart_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='clothings',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='gaming',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='healthandbeauty',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='homeandoffice',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='phoneandaccessories',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]