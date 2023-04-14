from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)