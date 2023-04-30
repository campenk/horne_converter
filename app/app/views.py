from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, MeasurementType


def converter(request, entry, unit, output_category):
    unit_category = MeasurementType.objects.filter()
    a_list = Item.objects.filter()
    return render(request, 'news/year_archive.html', a_list)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
