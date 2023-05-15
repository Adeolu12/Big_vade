# Generated by Django 3.2.18 on 2023-05-15 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20230515_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('clothings', 'Clothings'), ('phone_and_accessories', 'PhoneAndAccessories'), ('home_and_office', 'HomeAndOffice'), ('health_and_beauty', 'HealthAndBeauty'), ('gaming', 'Gaming')], max_length=225, null=True, verbose_name='Categories')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('price', models.CharField(blank=True, max_length=225, null=True)),
                ('in_stock', models.IntegerField(blank=True, null=True)),
                ('image_name', models.CharField(blank=True, max_length=225, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]