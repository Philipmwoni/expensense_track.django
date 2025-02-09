from django.shortcuts import render
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')


def homepage(request):
    return render(request, 'homepage.html')

def register(request):



    return render(request, 'register.html')



def login(request):

    return render(request, 'login.html')



def delete(request):
    return render(request, 'delete.html')




