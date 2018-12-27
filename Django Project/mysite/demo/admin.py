from django.contrib import admin
from demo.models import LoginUser

# Register your models here.
class LoginUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'account', 'img', 'data']

admin.site.register(LoginUser, LoginUserAdmin)
