from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'name']

class DepositForm (ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user', 'name']

class WalletForm (ModelForm):
    class Meta:
        model = Wallet
        fields = '__all__'
        exclude = ['user', 'name']

class AlertForm (ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        exclude = ['user', 'name']


class PinForm (ModelForm):
    class Meta:
        model = Pin
        fields = '__all__'
        exclude = ['user', 'name']
    
class WithdrawForm (ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction1Form (ModelForm):
    class Meta:
        model = Transaction1
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction2Form (ModelForm):
    class Meta:
        model = Transaction2
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction3Form (ModelForm):
    class Meta:
        model = Transaction3
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction4Form (ModelForm):
    class Meta:
        model = Transaction4
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction5Form (ModelForm):
    class Meta:
        model = Transaction5
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction6Form (ModelForm):
    class Meta:
        model = Transaction6
        fields = '__all__'
        exclude = ['user', 'name']

class Transaction7Form (ModelForm):
    class Meta:
        model = Transaction7
        fields = '__all__'
        exclude = ['user', 'name']
