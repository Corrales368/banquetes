from django.db import models

from apps.customers.models import Customer

    
class Banquet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='banquets')
    numer_of_guests = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms')
    banquet = models.ForeignKey(Banquet, on_delete=models.CASCADE, related_name='rooms')

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


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    banquet = models.ForeignKey(Banquet, on_delete=models.CASCADE, related_name='plans')
    food_choices = models.ManyToManyField(Food, related_name='plans')
    decoration_choices = models.ManyToManyField(Decoration, related_name='plans')
    entertainment_choices = models.ManyToManyField(Entertainment, related_name='plans')

    def __str__(self):
        return self.name
    
    @property
    def get_total_price(self):
        total_price = self.price
        for food in self.food_choices.all():
            total_price += food.price * self.banquet.numer_of_guests
        for decoration in self.decoration_choices.all():
            total_price += decoration.price * self.banquet.numer_of_guests
        for entertainment in self.entertainment_choices.all():
            total_price += entertainment.price * self.banquet.numer_of_guests
        return total_price

    def save(self, *args, **kwargs):
        print(self.get_total_price)
        super().save(*args, **kwargs)
    

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} - {self.plan}"
    

