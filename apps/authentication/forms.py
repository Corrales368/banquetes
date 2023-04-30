from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
)

from apps.shared.forms import BaseForm


class MyAuthenticationForm(BaseForm, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Email"
        self.fields["password"].label = "Contraseña"
        self.fields["username"].widget.attrs.update({"type": "email"})  
        self.fields["username"].widget.attrs.update({"placeholder": "Email"})
        self.fields["password"].widget.attrs.update({"placeholder": "Contraseña"})