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

    def save(self, commit=False):
        user = super().save(commit=False)

        # Check if the password need to be set (if changed or new user)
        if (
            User.objects.filter(id=user.id).exists()
            and User.objects.get(id=user.id).password != self.cleaned_data["password"]
        ) or self.instance._state.adding:
            user.set_password(self.cleaned_data["password"])

        if self.cleaned_data["groups"]:
            user.is_staff = self.cleaned_data["groups"][0].name == "managers"
        if commit:
            user.save()
        return user
