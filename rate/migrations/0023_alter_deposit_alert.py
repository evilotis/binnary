# Generated by Django 5.0.6 on 2024-05-21 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0022_alter_deposit_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='alert',
            field=models.CharField(choices=[('sweetAlert', 'sweetAlert'), ('trap', 'trap')], default='sweetAlert', max_length=24),
        ),
    ]
