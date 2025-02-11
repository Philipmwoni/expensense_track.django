from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_expense', views.create_expense, name='create_expense'),
    path('edit_expense/<str:pk>', views.edit_expense, name='edit_expense'),
    path('delete_expense/<str:pk>', views.delete_expense, name='delete_expense'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('delete', views.delete, name='delete'),

]
