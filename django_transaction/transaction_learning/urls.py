from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:account_name>/deposit", views.make_deposit_transaction, name="deposit"),
    path("<str:account_name>/withdraw", views.make_withdraw_transaction, name="withdraw"),
    path("<str:account_name>/send", views.make_sending_transaction, name="sending")
    

]