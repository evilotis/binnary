from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(customer_profile, sender=User)

def deposit(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(deposit, sender=User)

def wallet(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='wallet')
        instance.groups.add(group)
        Wallet.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(wallet, sender=User)

