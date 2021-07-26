from django.db import models
from django import forms
from django.core.validators import MinValueValidator

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=256)
    balance = models.FloatField(validators=[MinValueValidator(0.0)])

class LogTransaction(models.Model):
    account = models.CharField(max_length=256)
    transaction_type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)


class DepositForm(forms.Form):
    amount = forms.FloatField()

class WithdrawForm(forms.Form):
    amount = forms.FloatField()


class SendingForm(forms.Form):
    receive_account = forms.CharField(label="To Account", max_length=256)
    amount = forms.FloatField(label="Amount")
    


