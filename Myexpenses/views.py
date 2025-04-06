from django.shortcuts import render, redirect
from .models import Expenses, User_name, savings
from .form import ExpenseForm
from .serializers import ExpenseSerializer, savingsSerializer, User_nameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
import json


# API VIEWS
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def expense_list(request):
    expenses = Expenses.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


class SavingsCreateView(generics.ListAPIView):
    queryset = savings.objects.all()
    serializer_class = savingsSerializer


class User_nameViewSet(viewsets.ModelViewSet):
    queryset = User_name.objects.all()
    serializer_class = User_nameSerializer


# FORM'S VALIDATIONS
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
