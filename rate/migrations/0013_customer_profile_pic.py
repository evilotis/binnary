# Generated by Django 5.0.6 on 2024-05-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0012_rename_name_customer_bitcoin_wallet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avater.png', null=True, upload_to=''),
        ),
    ]
