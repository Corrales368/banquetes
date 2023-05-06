from django.contrib import admin

from apps.banquets import models


# admin.site.register(models.Banquet)
# admin.site.register(models.Food)
# admin.site.register(models.Decoration)
# admin.site.register(models.Entertainment)
# admin.site.register(models.Booking)
# admin.site.register(models.State)
# admin.site.register(models.City)
# admin.site.register(models.Location)
# admin.site.register(models.BanquetCustomerFood)
# admin.site.register(models.BanquetCustomerDecoration)
# admin.site.register(models.BanquetCustomerEntertainment)


@admin.register(models.Banquet)
class BanquetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Decoration)
class DecorationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Entertainment)
class EntertainmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass


class BanquetCustomerFoodInline(admin.TabularInline):
    model = models.BanquetCustomerFood
    extra = 1


class BanquetCustomerDecorationInline(admin.TabularInline):
    model = models.BanquetCustomerDecoration
    extra = 1


class BanquetCustomerEntertainmentInline(admin.TabularInline):
    model = models.BanquetCustomerEntertainment
    extra = 1


@admin.register(models.BanquetCustomer)
class BanquetCustomerAdmin(admin.ModelAdmin):
    inlines = [
        BanquetCustomerFoodInline,
        BanquetCustomerDecorationInline,
        BanquetCustomerEntertainmentInline,
    ]
    