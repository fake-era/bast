from django.db import models

from apps.book.models import Author, Genre, Review
from apps.user.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    author = models.ManyToManyField(Author, related_name='book_author')
    genre = models.ManyToManyField(Genre, related_name='book_genre')
    favourite = models.ManyToManyField(User, related_name='book_favourite')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        return Review.objects.filter(book=self)

    @property
    def rating(self):
        reviews = self.review_set.all()
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0
