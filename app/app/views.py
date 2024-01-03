from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .form import UserEntryForm
from .models import Item, MeasurementType, ItemCategory


# def converter(request, entry, unit, output_category):
#     unit_category = MeasurementType.objects.filter()
#     a_list = Item.objects.filter()
#     return render(request, 'news/year_archive.html', a_list)


def index(request):

    categories = ItemCategory.objects.all()
    template = loader.get_template('app/home.html')

    context = {
        'categories': categories,
    }

    if request.method == 'POST':
        form = UserEntryForm(request.POST)

        context['form-valid'] = form.is_valid()
        context['data'] = request.POST.items()
        context['user_entry'] = request.POST.get('user_entry')
        context['unit_choice'] = request.POST.get('unit_choice')
        context['output_options'] = request.POST.get('output_options')

        if form.is_valid():
            if unit_category(context['unit_choice']) == "length":
                context['result'] = convert_length_to_cm(context['user_entry'], context['unit_choice'])
            elif unit_category(context['unit_choice']) == "weight":
                context['result'] = convert_weight_to_kg(context['user_entry'], context['unit_choice'])

            context['result'] = categories

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
