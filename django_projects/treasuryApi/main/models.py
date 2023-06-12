from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return f'{self.name}'


class MethodPayment(models.Model):
    pay_method = models.CharField(max_length=100)
    percent_method = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.pay_method}: {self.percent_method}'


class Income(models.Model):
    income_amount = models.DecimalField(max_digits=15, decimal_places=2)
    pay_from = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name='Partners')
    sum_expend_for_delivery = models.DecimalField(max_digits=12, decimal_places=2,
                                                  null=True, blank=True)
    method_payment = models.ForeignKey(MethodPayment, on_delete=models.CASCADE, null=True,
                                       related_name='method_payments')
    real_date_payment = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.pay_from}: {self.income_amount}'


class MonthExpenses(models.Model):
    item_of_expend = models.CharField(max_length=100)
    sum_of_month_expend = models.DecimalField(max_digits=12, decimal_places=2,
                                              null=True, blank=True)

    class Meta:
        verbose_name = 'MonthExpense'
        verbose_name_plural = 'MonthExpenses'

    def __str__(self):
        return f'{self.item_of_expend}: {self.sum_of_month_expend}'
