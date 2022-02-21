from django.db import models


# Create your models here.
class Author (models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        author = self.last_name + ', ' + self.first_name
        return author


class Genre (models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre


class List(models.Model):
    list_title = models.CharField(max_length=255)

    def __str__(self):
        return self.list_title


class Book (models.Model):
    isbn = models.CharField(max_length=17, blank=True, null=True, verbose_name="ISBN")
    title = models.CharField(max_length=255)
    goodreads_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    library_availability = models.CharField(max_length=50, blank=True, null=True)
    # TODO to be integrated with Kotui API?
    READ = 'RE'
    CURRENTLY_READING = 'CU'
    TO_READ = 'TO'
    READ_STATUS_CHOICES = [
        (READ, 'Read'),
        (TO_READ, 'To Read'),
        (CURRENTLY_READING, 'Currently Reading')
    ]

    read_status = models.CharField(max_length=2, choices=READ_STATUS_CHOICES, default=TO_READ)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, default=0)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=0, blank=True, null=True)
    list = models.ForeignKey(List, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title
