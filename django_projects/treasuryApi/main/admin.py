from django.contrib import admin

from .models import *

admin.site.register(Partners)


@admin.register(Income)
class Incomes(admin.ModelAdmin):
    list_display = ('income_amount', 'pay_from', 'method_payment',
                    'sum_expend_for_delivery', 'real_date_payment')


@admin.register(MethodPayment)
class MethodPayments(admin.ModelAdmin):
    list_display = ('pay_method', 'percent_method')


@admin.register(MonthExpenses)
class MonthExpenses(admin.ModelAdmin):
    list_display = ('item_of_expend', 'sum_of_month_expend')
