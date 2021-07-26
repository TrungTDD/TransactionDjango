from django.contrib import admin
from .models import Account, LogTransaction
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    fields = ['name', "balance"]
    list_display = ["name", "balance"]

class LogTransactionAdmin(admin.ModelAdmin):
    fields = [ "account",
                    "transaction_type",
                    "status",
                    "message",
                    "created_at"]

    list_display = [ "account",
                    "transaction_type",
                    "status",
                    "message",
                    "created_at"]

admin.site.register(Account, AccountAdmin)
admin.site.register(LogTransaction, LogTransactionAdmin)
