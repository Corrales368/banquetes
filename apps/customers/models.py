import uuid

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    