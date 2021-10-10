from django.db import models
from django.contrib.auth.models import User


class BudgetItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.DecimalField(decimal_places=2, max_digits=10)
