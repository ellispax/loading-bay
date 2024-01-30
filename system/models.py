from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import TruncMonth
from django.db.models import Sum

# Create your models here.

class Equipment(models.Model):
    name                = models.CharField(max_length=255)
    make                = models.CharField(max_length=150)
    model               = models.CharField(max_length=150)
    man_year            = models.DateField()
    status              = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.make}  {self.name}'

class Operators(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, related_name="opr_username")
    name                = models.CharField(max_length=150)
    phoneNumber         = models.CharField(max_length=15)
    address             = models.CharField(max_length=150)
    machine             = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="mch_op_name")

    def __str__(self):
        return f'{self.name}'


class WorkLog(models.Model):
    machine             = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="log_machine_name")
    customerName        = models.CharField(max_length=100)
    phoneNumber         = models.CharField(max_length=15, default='+263xxxxxxxxx')
    date                = models.DateField()
    openingHr           = models.DecimalField(max_digits=20, decimal_places=2)
    closingHr           = models.DecimalField(max_digits=20, decimal_places=2)
    start_time          = models.TimeField(null = False, blank = False)
    end_time            = models.TimeField(null=True, blank=True)
    start_diesel        = models.IntegerField(null=False, blank=False)
    end_diesel          = models.IntegerField(null=True, blank=True)
    Fuel                = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    amnt_earned         = models.FloatField(null=True, blank=True)
    comment             = models.CharField(max_length=255, null=True, blank=True)
    paid                = models.BooleanField(default= True)


class MoveLog(models.Model):
    machine             = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="mvlog_machine_name")
    date                = models.DateField()
    openingHr           = models.DecimalField(max_digits=20, decimal_places=2)
    closingHr           = models.DecimalField(max_digits=20, decimal_places=2)
    depart_from         = models.CharField(max_length=100)
    destination         = models.CharField(max_length=100)
    comment             = models.CharField(max_length=255, null=True, blank=True)


class DieselPurchase(models.Model):
    machine             = models.ForeignKey(Equipment,on_delete=models.CASCADE, related_name="d_machine_name")
    receiptNumber       = models.CharField(max_length = 100, unique=True)
    date                = models.DateField()
    supplier            = models.CharField(max_length = 50)
    unit_price          = models.DecimalField(max_digits = 10, decimal_places=2)
    total_cost          = models.DecimalField(max_digits = 10, decimal_places=2)
    litres              = models.DecimalField(max_digits = 10, decimal_places=2, null = True, blank=True)


    def save(self, *args, **kwargs):
        # Calculate liters of fuel purchased based on unit price and total cost
        if self.unit_price and self.total_cost:
            self.litres = self.total_cost / self.unit_price
        else:
            self.litres = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Fuel Purchase - ID: {self.pk}, Liters: {self.litres}"
    
    

class OtherExpenses(models.Model):
    machine             = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name = "ex_machine")
    receiptNumber       = models.CharField(max_length = 100)
    date                = models.DateField()
    service             = models.CharField(max_length = 150)
    serviceProvider     = models.CharField(max_length = 150)
    total_cost          = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"Expense ID: {self.pk}, Cost: {self.liters_purchased}, Service: {self.service}"