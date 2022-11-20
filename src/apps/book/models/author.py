from django.db import models

from apps.book.models.book import Book


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    book = models.ManyToManyField(Book, related_name='author_book')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name
