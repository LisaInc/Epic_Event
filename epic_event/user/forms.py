from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = (
            "is_staff",
            "is_superuser",
            "last_login",
            "is_active",
            "date_joined",
            "user_permissions",
        )
