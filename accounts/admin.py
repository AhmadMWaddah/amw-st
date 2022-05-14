from django.contrib import admin

from accounts.models import Account, Address


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
