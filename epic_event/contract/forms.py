from forms import ModelForm
from .models import Contract
from user.models import User
from django.contrib.auth.models import Group


class ContractForm(ModelForm):
    def __init__(self, company, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        print(User.objects.filter(groups_name="sales"))
        self.fields["sale_contact"].queryset = User.objects.filter(groups_name="sales")

    class Meta:
        model = Contract
