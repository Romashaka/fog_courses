from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.CharField(max_length=200)
    date_of_birth = models.DateField(
            blank=True, null=True)

    def __str__(self):
        return self.author


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title
