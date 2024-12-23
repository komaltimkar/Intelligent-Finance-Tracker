from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
#from .models import Transaction
from django.utils.timezone import now
from datetime import datetime
def parse_datetime(date_string):
    if isinstance(date_string, str):
        try:
            return datetime.fromisoformat(date_string)
        except ValueError:
            print("Invalid date string format.")
            return None
    else:
        print("The argument must be a string.")
        return None
#admin.site.register(Transaction)
class Transaction(models.Model):
    class Meta:
        db_table = 'expenses_transaction'


class SavingsGoal(models.Model):
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Savings Goal: ₹{self.goal_amount}, Current Savings: ₹{self.current_savings}"
# models.py

from django.contrib.auth.models import User
from django.db import models



'''class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES,default='Expense')
    description = models.CharField(max_length=255,default='No description provided')
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)'''
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES,default='Expense')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"


