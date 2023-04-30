from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from apps.users.models import LoginActivity


@receiver(user_logged_in)
def login_activity(sender, request, user, **kwargs):
    """
    Create a login activity when a user logs in.
    """
    LoginActivity.objects.create(user=user)