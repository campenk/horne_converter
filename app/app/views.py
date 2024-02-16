from decimal import Decimal

from django.template.response import TemplateResponse

from .form import UserEntryForm
from .models import Item, ItemCategory
import random
from .constants import WEIGHT_UNITS, LENGTH_UNITS, CONVERSION_FACTORS
import humanize


def index(request):

    context = {}

    if request.method == 'POST':
        form = UserEntryForm(request.POST)

        if form.is_valid():
            #  determine measurement type
            measurement_type = _unit_category(form.cleaned_data['input_unit'])
            print("measurement type = " + measurement_type)

            #  calculate standardized value
            standardized_value = _convert_to_standardized_value(form.cleaned_data['input_unit'], float(form.cleaned_data['input_value']), measurement_type)

            #  get list of items that are in output category
            items_in_category = _get_items_in_category(form.cleaned_data['output_category'], measurement_type)
            items_whole_number = []

            #  create list of items where the modulo is zero and the quotient is > 1
            for item in items_in_category:
                if _is_modulo_zero(standardized_value, item) and _is_greater_than_one(standardized_value, item):
                    items_whole_number.append(item)

            #  return random item
            #  Preferentially return items where the modulo is zero and the quotient is > 1
            if not items_whole_number:
                output_unit = random.choice(items_in_category)
            else:
                output_unit = random.choice(items_whole_number)

            output_value = Decimal(standardized_value) / output_unit.item_measurement
            print(output_value)
            if output_value > 1:
                output_value = round(output_value, 0)

            result = (
                    str(_humanize_input(form.cleaned_data['input_value'])) + " " +
                    form.cleaned_data['input_unit'] + " is equal to "
                    + str(_humanize_output(output_value)) + " "
                    + output_unit.item_name + "s ")
            context['result'] = result

    else:
        form = UserEntryForm()

    context['form'] = form
    return TemplateResponse(request, 'app/home.html', context)


def _unit_category(unit):

    for i in WEIGHT_UNITS:
        if i[0] == unit:
            return "WE"
    for i in LENGTH_UNITS:
        if i[0] == unit:
            return "LE"


def _convert_length_to_m(user_input: float, unit: str) -> float:

    for i in CONVERSION_FACTORS:
        if unit == i[0]:
            print("length in m = " + str(user_input * i[1]))
            return user_input * i[1]


def _convert_weight_to_g(user_input: float, unit: str) -> float:

    for i in CONVERSION_FACTORS:
        if unit == i[0]:
            print("weight in g = " + str(user_input * i[1]))
            return user_input * i[1]


def _convert_to_standardized_value(input_unit, input_value, unit_category):
    if unit_category == "LE":
        return _convert_length_to_m(input_value, input_unit)
    else:
        return _convert_weight_to_g(input_value, input_unit)


def _get_items_in_category(output_category, measurement_type):
    print("output category = " + str(output_category))
    print(Item.objects.all())
    qs = (
        Item.objects.filter(
            measurement_type=measurement_type)
    )

    if output_category is None:
        print(qs)
        return qs

    else:
        return qs.filter(
            item_category=ItemCategory.objects.get(
                item_category=output_category))


def _is_modulo_zero(standardized_value, item):
    modulo = Decimal(standardized_value) % item.item_measurement
    if round(modulo, 0) == 0:
        return True
    else:
        return False


def _is_greater_than_one(standardized_value, item):
    if Decimal(standardized_value) / item.item_measurement >= 1:
        return True
    else:
        return False


def _humanize_output(output):
    if output >= 1000000:
        return humanize.intword(output)
    elif output >= 1000:
        return humanize.intcomma(output)
    elif 1 <= output <= 10:
        return humanize.apnumber(output)
    elif output < 1:
        return humanize.fractional(output)
    else:
        return output


def _humanize_input(input):
    if input >= 1000000:
        return humanize.intword(input)
    elif input >= 1000:
        return humanize.intcomma(input)
    else:
        return input