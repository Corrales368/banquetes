from django.db import models

# Create your models here.

class Lounge(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self) -> str:
        return f"{self.id}"