from user.models import User


class UserPermission:
    def is_sales(self, user):
        return bool(User.objects.filter(user=user, group="Sales"))

    def is_support(self, user):
        return bool(User.objects.filter(user=user, group="Support"))

    def is_manager(self, user):
        return bool(User.objects.filter(user=user, group="Management"))
