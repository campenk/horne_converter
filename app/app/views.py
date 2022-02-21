from django.shortcuts import render
from django.http import HttpResponse
from .models import List


# Create your views here.
def all_lists(request):
    list_index = List.objects.order_by('-year')
    output = ', '.join([q.list_title for q in list_index])
    return HttpResponse(output)


def list_detail(request, list_id):
    return HttpResponse("You're looking at list %s." % list_id)


def book_detail(request, book_id):
    return HttpResponse("You're looking at question %s." % book_id)


def author_detail(request, author_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % author_id)


def genre_detail(request, genre_id):
    return HttpResponse("You're voting on question %s." % genre_id)
