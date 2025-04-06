from rest_framework import serializers
from .models import Expenses, savings, User_name


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class savingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=savings
        fields = '__all__'



class User_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_name
        fields = '__all__'