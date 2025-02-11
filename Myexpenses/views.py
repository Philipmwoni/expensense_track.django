from django.shortcuts import render, redirect
from .models import Expenses, User_name
from .form import ExpenseForm
import json


# Create your views here.

def home(request):
    expenses = Expenses.objects.all()
    username = User_name.objects.all()
    data = {'expenses': expenses, 'username': username}
    return render(request, 'home.html', data)


def create_expense(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'create_expense.html', {'form': ExpenseForm()})


def edit_expense(request, pk):
    expense = Expenses.objects.get(id=pk)
    form = ExpenseForm(instance=Expenses)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=Expenses)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create_expense.html', context)


def delete_expense(request, pk):
    expense = Expenses.objects.get(id=pk)


def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def delete(request):
    return render(request, 'delete.html')
