from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Client
from .forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        kwargs["form"] = UserForm
        return super().get_form(request, obj, **kwargs)

    def create(self, request, obj, form, change):
        print(form["password"].value())
        obj.set_password(form["password"].value())
        obj.save()
        obj.is_staff = bool(obj.groups.filter(name="management"))
        obj.save()


admin.site.register(Client)
# admin.site.unregister(Group)
