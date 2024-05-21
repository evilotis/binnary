from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


kyc = (
    ('$', '$'),
    ('£ ', '£'),
    ('€', '€'),
    )


class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    first_name = models.CharField (max_length = 200,  null = True)
    last_name = models.CharField (max_length = 200,  null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)
    bitcoin_wallet = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)

    def __str__(self):
        return str(self.name)

alert = (
    ('sweetAlert', 'sweetAlert'),
    ('stop1',"stop1"),
    )
class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    active_deposit = models.CharField (max_length = 200, null = True, default='0')
    main_deposit = models.CharField (max_length = 200, null = True, default='0')
    added_bonus = models.CharField (max_length = 200, null = True, default='0')
    withdraw_funds = models.CharField (max_length=24, null = True, default='0.00')
    currency = models.CharField (max_length=24, choices=kyc, default='$')
    alert = models.CharField (max_length=24, choices=alert, default='sweetAlert')


    def __str__(self):
        return str(self.name)


class Wallet (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    wallet = models.CharField (max_length = 200, null = True, default='0')

    def __str__(self):
        return str(self.name)


choices = [
    ('sweetAlert', 'sweetAlert'),
    ('paid',"paid"),
]
    
STATUS = (
    ('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('KYC has not been uploaded kindly contact customercare for more information', 'KYC has not been uploaded kindly contact customercare for more information'),
    )

class Alert (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    alert = models.CharField (max_length=24, choices=choices, default='sweetAlert')
    status = models.CharField (max_length=200, null=True, choices=STATUS, default='You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.')

    def __str__(self):
        return str(self.name)


class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)


statu = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    )

type = (
    ('bitcoin', 'bitcoin'),
    ('transfer', 'transfer'),
    ('cashapp', 'cashapp'),
    ('skril', 'skril'),
    ('Western Union', 'Western Union'),
    ('paypal', 'paypal'),
    )


class Withdraw (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True, choices=statu, default='Pending')
    transaction_id = models.CharField (max_length=200, null=True)
    type = models.CharField (max_length=200, null=True, choices=type)

    def __str__(self):
        return str(self.name)

class Transaction1 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)

class Transaction2 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)

class Transaction3 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)

class Transaction4 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)

class Transaction5 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)

class Transaction6 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)

class Transaction7 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True)


    def __str__(self):
        return str(self.name)