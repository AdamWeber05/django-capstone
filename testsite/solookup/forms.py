from django import forms
from django.forms import ModelForm
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

from .models import Boat

# On date fields, generate Date Widget
# @param:   forms.DateInput -> built-in Date Input widget
class DateInput(forms.DateInput):
    input_type = 'date'

# Form to create a new Boat
# @param:   ModelForm -> built-in Model form to update Django Models
class BoatForm(ModelForm):
    class Meta:
        model = Boat
        fields = ['model', 'so_num', 'serial_num', 'color', 'dealer_name', 'motor', 'anticipated_Start']
        widgets = {'anticipated_Start' : DateInput()}
