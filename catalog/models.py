from django.db import models


class Authors(models.Model):
    """
    Author Model
    Defines the attributes of a author
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Books(models.Model):
    """
    Book Model
    Defines the attributes of a book
    """
    name = models.CharField(max_length=255)
    edition = models.IntegerField()
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Authors)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
