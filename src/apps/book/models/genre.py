from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name
