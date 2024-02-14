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

#  Unit abbreviation, unit name, conversion factor to metres
LENGTH_UNITS = [
    (MILLIMETRES, "Millimetres"),
    (CENTIMETRES, "Centimetres"),
    (METRES, "Metres"),
    (KILOMETRES, "Kilometres"),
    (MILES, "Miles"),
    (YARDS, "Yards"),
    (FEET, "Feet"),
    (INCHES, "Inches")
]

#  Unit abbreviation, unit name, conversion factor to grams
WEIGHT_UNITS = [
    (KILOGRAMS, "Kilograms"),
    (GRAMS, "Grams"),
    (MILLIGRAMS, "Milligrams"),
    (POUNDS, "Pounds"),
    (OUNCES, "Ounces")
]

UNIT_CHOICES = [
    ]

for i in WEIGHT_UNITS:
    UNIT_CHOICES.append(i)
for i in LENGTH_UNITS:
    UNIT_CHOICES.append(i)

CONVERSION_FACTORS = [
    (MILLIMETRES, 0.001),
    (CENTIMETRES, 0.01),
    (METRES, 1),
    (KILOMETRES, 1000),
    (MILES, 1609),
    (YARDS, 1.0936),
    (FEET, 0.3048),
    (INCHES, 0.0254),
    (KILOGRAMS, 1000),
    (GRAMS, 1),
    (MILLIGRAMS, 0.001),
    (POUNDS, 453.592),
    (OUNCES, 28.3495)
]
