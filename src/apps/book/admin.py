from django.contrib import admin

from apps.book.models import Book, Review, Author, Genre

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Author)
admin.site.register(Genre)
