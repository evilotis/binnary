# Generated by Django 5.0.6 on 2024-05-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0011_transaction1_transaction2_transaction3_transaction4_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='bitcoin_wallet',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='currency',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
