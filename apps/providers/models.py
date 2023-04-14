from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()
    photo = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"
