# Generated by Django 5.0.6 on 2024-05-15 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_alter_customer_currency'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('active_deposit', models.CharField(default='0', max_length=200, null=True)),
                ('main_deposit', models.CharField(default='0', max_length=200, null=True)),
                ('added_bonus', models.CharField(default='0', max_length=200, null=True)),
                ('withdraw_funds', models.CharField(default='0.00', max_length=24, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
