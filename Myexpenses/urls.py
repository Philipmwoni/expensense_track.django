from django.urls import path, include
from . import views
from .views import User_nameViewSet, SavingsCreateView, expense_list
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reviews', User_nameViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('create_expense', views.create_expense, name='create_expense'),
    path('edit_expense/<str:pk>', views.edit_expense, name='edit_expense'),
    path('delete_expense/<str:pk>', views.delete_expense, name='delete_expense'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('delete', views.delete, name='delete'),
    path('api/expenses/<str:pk>/', expense_list, name='expense/api'),
    path('savings/', SavingsCreateView.as_view(), name='savings'),
    path('api/User_name/', include(router.urls)),

]
