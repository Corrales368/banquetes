from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()
    photo = models.ImageField(upload_to="customers", null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/avatar/user_avatar.jpg"