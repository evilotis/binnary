from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
from .models import *

def index(request):
    context = {}
    return render (request, "rate/index.html", context)

def about(request):
    context = {}
    return render (request, "rate/about.html", context)

def account(request):
    context = {}
    return render (request, "rate/account.html", context)


def forget_password(request):
    context = {}
    return render (request, "rate/forget_password.html", context)

def plans(request):
    context = {}
    return render (request, "rate/plans.html", context)

def rbc(request):
    context = {}
    return render (request, "rate/rbc.html", context)

@login_required (login_url = "login")
def deposit_history(request):
    context = {}
    return render (request, "rate/deposit_history.html", context)

@login_required (login_url = "login")
def referals(request):
    context = {}
    return render (request, "rate/referals.html", context)

def logoutUser(request):
    logout (request)
    return redirect ('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('account')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('account')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "rate/login.html", context)

def security(request):
    context = {}
    return render (request, "rate/security.html", context)

@login_required (login_url = "login")
def withdrawal(request):
    context = {}
    return render (request, "rate/withdrawal.html", context)

@login_required (login_url = "login")
def wealth(request):
    context = {}
    return render (request, "rate/wealth.html", context)

@login_required (login_url = "login")
def transaction_history(request):
    context = {}
    return render (request, "rate/transaction_history.html", context)

@login_required (login_url = "login")
def process_payment(request):
    context = {}
    return render (request, "rate/process_payment.html", context)


@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('login')

    context = {'form': form}
    return render (request, "rate/register.html", context)

def terms(request):
    context = {}
    return render (request, "rate/terms.html", context)

@login_required (login_url = "login")
def withdrawal_history(request):
    context = {}
    return render (request, "rate/withdrawal_history.html", context)

@login_required (login_url = "login")
def pin(request):
    context = {}
    return render (request, "rate/pin.html", context)


@login_required (login_url = "login")
def details(request):
    context = {'form': form}
    return render (request, "rate/details.html", context)

@login_required (login_url = "login")
def processing(request):
    context = {}
    return render (request, "rate/processing.html", context)

@login_required (login_url = "login")
def plan(request):
    context = {}
    return render (request, "rate/plan.html", context)

@login_required (login_url = "login")
def profile(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "rate/profile.html", context)

@login_required (login_url = "login")
def change_password(request):
    context = {}
    return render (request, "rate/change_password.html", context)

@login_required (login_url = "login")
def deposit(request):
    context = {}
    return render (request, "rate/deposit.html", context)

