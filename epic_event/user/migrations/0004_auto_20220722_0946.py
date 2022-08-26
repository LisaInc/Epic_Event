# Generated by Django 4.0.6 on 2022-07-22 09:46

from django.db import migrations


def create_groups(apps, schema_migration):
    Group = apps.get_model("auth", "Group")
    supports = Group(name="supports")
    supports.save()

    sales = Group(name="sales")
    sales.save()

    managers = Group(name="managers")
    managers.save()


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_user_team"),
    ]

    operations = [migrations.RunPython(create_groups)]
