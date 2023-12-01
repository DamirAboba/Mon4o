# models.py
from django.db import models
from django.contrib.auth.models import User


class Cabinet(models.Model):
    number = models.IntegerField(unique=True)
    cabinet_key = models.PositiveIntegerField(unique=True, default=1)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)


class UserActivity(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cabinet {self.cabinet.number} Activity"
