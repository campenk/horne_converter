from django import forms
from .models import ItemCategory


class UserEntryForm(forms.Form):
    MILLIMETRES = "MM"
    CENTIMETRES = "CM"
    METRES = "M"
    KILOMETRES = "KM"
    MILES = "MI"
    YARDS = "Y"
    FEET = "FT"
    INCHES = "IN"
    KILOGRAMS = "KG"
    GRAMS = "G"
    MILLIGRAMS = "MG"
    POUNDS = "LB"
    OUNCES = "OZ"
    UNIT_CHOICES = [
        ('Length', (
            (MILLIMETRES, "Millimetres"),
            (CENTIMETRES, "Centimetres"),
            (METRES, "Metres"),
            (KILOMETRES, "Kilometres"),
            (MILES, "Miles"),
            (YARDS, "Yards"),
            (FEET, "Feet"),
            (INCHES, "Inches"),
        )
         ),
        ('Weight', (
            (KILOGRAMS, "Kilograms"),
            (GRAMS, "Grams"),
            (MILLIGRAMS, "Milligrams"),
            (POUNDS, "Pounds"),
            (OUNCES, "Ounces"),
        )
         ),
    ]

    user_entry = forms.DecimalField()
    unit_choice = forms.ChoiceField(choices=UNIT_CHOICES, label="unit")
    output_options = forms.ModelChoiceField(ItemCategory.objects.all())




