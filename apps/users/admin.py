from django.contrib import admin
from apps.users import models


admin.site.register(models.User)

@admin.register(models.LoginActivity)
class LoginActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "date_login")
    list_filter = ("user", "date_login")
    search_fields = ("user", "date_login")
