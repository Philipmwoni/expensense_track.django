from django.db import models


# Create your models here.


class Expenses(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} -{self.date}"


class savings(models.Model):
    name = models.CharField(max_length=256, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class User_name(models.Model):
    Expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    Name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    password = models.CharField(max_length=5, null=False, blank=False, unique=True)
    savings = models.ForeignKey(savings, on_delete=models.CASCADE)
