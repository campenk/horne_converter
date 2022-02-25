from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import List, Book, Author, Genre
from django.urls import reverse
from django.views import generic
from django.db import models
from django.db.models.functions import Concat
from django.db.models import CharField, Value, F, TextChoices
from django.template import loader


# Create your views here.
def all_lists(request):
    try:
        all_lists = List.objects.order_by('list_title')
    except List.DoesNotExist:
        raise Http404
    return render(request, 'all_lists.html', {'all_lists': all_lists})


def list_detail(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    books_in_list = (
        Book.objects
            .filter(list=list)
        #  can put the these into a model manager statement if used often
            .select_related('author')
            .select_related('genre')
            .select_related('list')
            .annotate(full_name=Concat(F('author__last_name'), Value(', '), F('author__first_name'),
                                       F('author__middle_name')))
    )

    return render(
        request,
        'view_list.html',
        context={
            'books_in_list': books_in_list,
            'list': list,
        }
    )

"""
def book_detail(request, book_id):
    
    try:

        book_detail = (
            Book.objects
            .filter(book_id=book_id)
            .select_related('author')
            .select_related('genre')
            .annotate(full_name=Concat(F('author__last_name'), Value(', '), F('author__first_name'),
                                           F('author__middle_name')))
        )
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'book_detail', {'book_detail': book_detail})

"""

class DetailView(generic.DetailView):
    model = Book
    template_name = book_detail.html


def author_detail(request, author_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % author_id)


def genre_detail(request, genre_id):
    return HttpResponse("You're voting on question %s." % genre_id)
