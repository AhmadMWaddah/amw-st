from django.contrib import admin
from .models import Account, ShippingDetail


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'staff', 'admin', 'superuser']
    list_editable = ['staff', 'admin', 'superuser']
    fieldsets = (
        ('Data', {'fields': ('username', 'email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('staff', 'admin', 'superuser')}),
    )


@admin.register(ShippingDetail)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account', 'mobile', 'type', 'address']
