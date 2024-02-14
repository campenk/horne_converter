from django import forms
from .models import ItemCategory
from .constants import UNIT_CHOICES


class UserEntryForm(forms.Form):

    input_value = forms.DecimalField()
    input_unit = forms.ChoiceField(choices=UNIT_CHOICES, label="unit")
    output_category = forms.ModelChoiceField(ItemCategory.objects.all(), empty_label="random", required=False)




