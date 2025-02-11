from django.contrib import admin
from .models import User_name, savings, Expenses


# Register your models here.
class UsernameAdmin(admin.ModelAdmin):
    search_fields = ('Name', 'created_at')


admin.site.register(User_name, UsernameAdmin)
admin.site.register(savings)
admin.site.register(Expenses)
