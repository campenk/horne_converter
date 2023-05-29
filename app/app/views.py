from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Item, MeasurementType, ItemCategory


# def converter(request, entry, unit, output_category):
#     unit_category = MeasurementType.objects.filter()
#     a_list = Item.objects.filter()
#     return render(request, 'news/year_archive.html', a_list)


def index(request):
    latest_question_list = "Q1", "Q2", "Q3"
    categories = ItemCategory.objects.all()
    template = loader.get_template('app/home.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    return HttpResponse("You are at the home view")

