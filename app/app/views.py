import decimal

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .form import UserEntryForm
from .models import Item, MeasurementType, ItemCategory
import random


# def converter(request, entry, unit, output_category):
#     unit_category = MeasurementType.objects.filter()
#     a_list = Item.objects.filter()
#     return render(request, 'news/year_archive.html', a_list)


def index(request):

    template = loader.get_template('app/home.html')

    # categories = ItemCategory.objects.filter(itemCategory=request.POST.get('output_options'))
    all_categories = ItemCategory.objects.all()


    context = {
        'categories': all_categories,
    }

    if request.method == 'POST':
        form = UserEntryForm(request.POST)

        context['form-valid'] = form.is_valid()
        context['data'] = request.POST.items()
        context['input_value'] = request.POST.get('input_value')
        context['input_unit'] = request.POST.get('input_unit')
        context['output_category'] = request.POST.get('output_category')
        context['modulo'] = ""

        if form.is_valid():
            #  create list of items matching output category
            if context['output_category'] == "":
                items_in_category = Item.objects.all()
            else:
                items_in_category = Item.objects.filter(itemCategory=ItemCategory.objects.get(id=context['output_category']))
            context['result'] = str(context['input_value']) + " " + context['input_unit']
            items_whole_number = []

            if unit_category(context['input_unit']) == "length":
                #  convert input value to standardized value
                standardized_value = convert_length_to_cm(context['input_value'], context['input_unit'])
                context['standardized_value'] = standardized_value

                #  select items that return a whole number
                for item in items_in_category:
                    if round(decimal.Decimal(standardized_value) % item.itemMeasurement, 0) == 0:
                        items_whole_number.append(item)

                #  check if there are any items that return a whole number
                if not items_whole_number:
                    output_unit = random.choice(items_in_category)
                    context['modulo'] += "no items return whole number"
                else:
                    output_unit = random.choice(items_whole_number)

                context['modulo'] += " 1 unit is " + str(round(output_unit.itemMeasurement, 0)) + " and modulo " + str(round(decimal.Decimal(standardized_value) % output_unit.itemMeasurement, 0))
                output_value = round(decimal.Decimal(standardized_value) / output_unit.itemMeasurement,0)
                context['result'] += " is equal to " + str(output_value) + " " + output_unit.itemName + "s"

            elif unit_category(context['input_unit']) == "weight":
                output_unit = random.choice(items_in_category)

                standardized_value = convert_weight_to_kg(context['input_value'], context['input_unit'])
                context['standardized_value'] = standardized_value
                context['modulo'] += "modulo " + str(round(decimal.Decimal(standardized_value) % output_unit.itemMeasurement, 1))
                output_value = round(decimal.Decimal(standardized_value) / output_unit.itemMeasurement,1)
                context['result'] += " is equal to " + str(output_value) + " " + output_unit.itemName + "s"


    else:
        form = UserEntryForm()

    context['form'] = form

    return HttpResponse(template.render(context, request))


def home(request):
    return HttpResponse("You are at the home view")


def unit_category(unit):
    #  can i just test for group name??
    if unit == "MM" or unit == "CM" or unit == "M" or unit == "KM" or unit == "MI" or unit == "Y" or unit == "FT" or unit == "IN":
        category = "length"
    else:
        # should i explicitly do an if statement for this?
        category = "weight"
    return category


def convert_length_to_cm(user_input, unit):
    user_input = int(user_input)
    match unit:
        case "CM":
            return user_input
        case "MM":
            return user_input / 10
        case "M":
            return user_input * 100
        case "KM":
            return user_input * 100000
        case "MI":
            return user_input * 160934
        case "Y":
            return user_input * 91.44
        case "FT":
            return user_input * 30.48
        case "IN":
            return user_input * 2.54


def convert_weight_to_kg(user_input, unit):
    user_input = int(user_input)
    match unit:
        case "KG":
            return user_input
        case "G":
            return user_input/1000
        case "MG":
            return user_input/1000000
        case "LB":
            return user_input*0.453592
        case "OZ":
            return user_input*0.0283495


def item_modulo_zero(output_category, standardized_value):
    #  TODO: Add if output is > 1
    items_whole_number = []
    if output_category == "":
        items_in_category = Item.objects.all()

    else:
        items_in_category = Item.objects.filter(itemCategory=ItemCategory.objects.get(id=output_category))

    for item in items_in_category:
        if round(decimal.Decimal(standardized_value) % item.itemMeasurement, 1) != 0 and round(decimal.Decimal(standardized_value) / item.itemMeasurement, 1) > 0:
            items_whole_number.append(item)

    if not items_whole_number:
        output_unit = random.choice(items_in_category)

    else:
        output_unit = random.choice(items_whole_number)

    return output_unit
