from django.db import models

# Create your models here.




class Expenses(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title





class savings(models.Model):
    amount = models.DecimalField(max_digits=20,decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


class User_name(models.Model):
    Expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    password = models.CharField(max_length=5, null=False, blank=False, unique=True)
    savings = models.ForeignKey(savings, on_delete=models.CASCADE)
