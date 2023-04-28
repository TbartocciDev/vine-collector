from django.forms import ModelForm
from .models import SoldDate

class SoldDateForm(ModelForm):
  class Meta:
    model = SoldDate
    fields = ['date', 'quantity']