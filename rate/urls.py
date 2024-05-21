from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('account/', views.account, name = "account"),
    path ('referals/', views.referals, name = "referals"),
    path ('forget_password/', views.forget_password, name = "forget_password"),
    path ('plans/', views.plans, name = "plans"),
    path ('plan/', views.plan, name = "plan"),
    path ('deposit_history/', views.deposit_history, name = "deposit-history"),
    path ('withdrawal/', views.withdrawal, name = "withdrawal"),
    path ('wealth/', views.wealth, name = "wealth"),
    path ('security/', views.security, name = "security"),
    path ('register/', views.register, name = "register"),
    path ('login/', views.loginPage, name = "login"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('terms/', views.terms, name = "terms"),
    path ('pin/', views.pin, name = "pin"),
    path ('profile/', views.profile, name = "profile"),
    path ('processing/', views.processing, name = "processing"),
    path ('process_payment/', views.process_payment, name = "process_payment"),
    path ('rbc/', views.rbc, name = "rbc"),
    path ('withdrawal_history/', views.withdrawal_history, name = "withdrawal_history"),
    path ('change_password/', views.change_password, name = "change_password"),
    path ('transaction_history/', views.transaction_history, name = "transaction_history"),
    path ('deposit/', views.deposit, name = "deposit"),
 ]