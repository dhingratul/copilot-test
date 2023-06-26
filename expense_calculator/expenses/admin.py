from django.contrib import admin

from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    These are the expense model fields that will be displayed in the admin panel
    list_display = ('name', 'amount', 'timestamp', 'category')
    list_filter = ('timestamp', 'category')
    search_fields = ('name', 'description')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    fields = ('name', 'amount', 'category', 'description')
    readonly_fields = ('timestamp',)
    """
    list_display = ('name', 'amount', 'timestamp', 'category')
    list_filter = ('timestamp', 'category')
    search_fields = ('name', 'description')