from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Client
from .forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        kwargs["form"] = UserForm
        return super().get_form(request, obj, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     user = super(UserViewSet, self).create(request, *args, **kwargs)
    #     user.is_staff = user["team"] == "management"
    #     user.save()
    #     print(user.is_staff)
    #     return user
    def save_model(self, request, obj, form, change):
        # print(obj.groups)
        print(form["password"])
        obj.set_password(validated_data["password"])

        obj.save()
        obj.is_staff = bool(obj.groups.filter(name="management"))

        obj.save()


# admin.site.register(User)
admin.site.register(Client)
# admin.site.unregister(Group)
