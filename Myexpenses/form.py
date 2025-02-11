from .models import Expenses
from django import forms


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['title', 'description', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
