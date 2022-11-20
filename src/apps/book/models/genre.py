from django.db import models

from apps.book.models.book import Book


class Genre(models.Model):
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book, related_name='genre_book')

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name
