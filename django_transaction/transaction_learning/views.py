from django.shortcuts import render
from .models import SendingForm, DepositForm, WithdrawForm, Account, LogTransaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError, transaction
# Create your views here.

DEPOSIT_TRANSACTION = "Deposit"
SENDING_TRANSACTION = "Sending"
WITHDRAW_TRANSACTION = "Withdraw"
ERROR_STATUS = "Error"
SUCCESSFULLY_STATUS = "Sucessfully"

def index(request):
    accounts = Account.objects.all()
    return render(request, "transaction_learning/index.html", {
        "accounts" : accounts
    })


def make_deposit_transaction(request, account_name):
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            account = Account.objects.get(name=account_name)
            account.balance += amount
            account.save()
            return HttpResponseRedirect(reverse("index"))
        
    return render(request, "transaction_learning/deposit.html",{
        "form" : DepositForm(),
        "account_name" : account_name
    })
    

def make_withdraw_transaction(request, account_name):
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            account = Account.objects.get(name=account_name)
            account.balance -= amount
            account.save()
            return HttpResponseRedirect(reverse("index"))

    return render(request, "transaction_learning/withdraw.html",{
        "form" : WithdrawForm(),
        "account_name" : account_name
    })


def make_sending_transaction(request, account_name):
    if request.method == "POST":        
        form = SendingForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    receive_account = form.cleaned_data.get("receive_account")
                    amount = form.cleaned_data.get("amount")

                    from_user = Account.objects.get(name=account_name)
                    from_user.balance -= amount
                    from_user.save()

                    # cố tình trigger amount < 0 sau khi save, để sử dụng transaction trong django
                    if from_user.balance < 0:
                        raise ValueError()

                    receive_user = Account.objects.get(name=receive_account)
                    receive_user.balance += amount
                    receive_user.save()
                    LogTransaction(account=account_name, message="TRANSACTION SUCCESSFULLY", 
                                transaction_type=SENDING_TRANSACTION, status=SUCCESSFULLY_STATUS).save()
                    return HttpResponseRedirect(reverse("index"))

            except Account.DoesNotExist:
                LogTransaction(account=account_name, message = "ERROR ON SENDING. RECEIVING ACCOUNT IS NOT EXISTS", 
                                transaction_type=SENDING_TRANSACTION, status=ERROR_STATUS).save()
                return HttpResponseRedirect(reverse("index"))

            except ValueError:
                LogTransaction(account=account_name, message = "ERROR ON SENDING. ACCOUNT NOT SUFFICIENT", 
                                transaction_type=SENDING_TRANSACTION, status=ERROR_STATUS).save()
                return HttpResponseRedirect(reverse("index"))

    return render(request, "transaction_learning/sending.html", {
        "form" : SendingForm(),
        "account_name" : account_name
    })


