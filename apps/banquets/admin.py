from django.contrib import admin

from apps.banquets import models


admin.site.register(models.Banquet)
admin.site.register(models.Food)
admin.site.register(models.Decoration)
admin.site.register(models.Entertainment)
admin.site.register(models.Plan)
admin.site.register(models.Booking)