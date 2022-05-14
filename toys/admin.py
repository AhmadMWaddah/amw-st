from django.contrib import admin

from toys.models import Toy, Category


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'sku', 'age', 'inventory', 'in_stock', 'price']
    list_editable = ['inventory', 'price', ]
    prepopulated_fields = {'slug': ('name', 'sku')}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
