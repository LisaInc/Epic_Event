from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Client
from .forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        kwargs["form"] = UserForm
        return super().get_form(request, obj, **kwargs)

    def change(self, request, obj, form, change):
        print(change)
        print(obj)
        obj.save()


admin.site.register(Client)
# admin.site.unregister(Group)
