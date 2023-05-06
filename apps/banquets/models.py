from django.db import models

from apps.customers.models import Customer


class Banquet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="banquets")
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Decoration(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Entertainment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BanquetCustomer(models.Model):
    banquet = models.ForeignKey(Banquet, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food, through="BanquetCustomerFood")
    decoration = models.ManyToManyField(Decoration, through="BanquetCustomerDecoration")
    entertainment = models.ManyToManyField(Entertainment, through="BanquetCustomerEntertainment")

    def __str__(self):
        return self.customer


class BanquetCustomerFood(models.Model):
    banquet_customer = models.ForeignKey(BanquetCustomer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.banquet_customer


class BanquetCustomerDecoration(models.Model):
    banquet_customer = models.ForeignKey(BanquetCustomer, on_delete=models.CASCADE)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.banquet_customer


class BanquetCustomerEntertainment(models.Model):
    banquet_customer = models.ForeignKey(BanquetCustomer, on_delete=models.CASCADE)
    entertainment = models.ForeignKey(Entertainment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.banquet_customer


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    banquet_customer = models.ForeignKey(BanquetCustomer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.customer
