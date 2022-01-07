from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='The name of the Publisher')
    website = models.URLField(help_text="The Publisher's website")


class Book(models.Model):
    title = models.CharField(max_length=70, help_text="The title of the book!")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name='ISBN number of the book.')


class Contributor(models.Model):
    """
    A Contributor to a book, e.g. author, editor, co-author
    """

    first_names = models.CharField(max_length=50, help_text="The contributor's first name of names")
    last_names = models.CharField(max_length=50, help_text="The Contributor's last name or names")
    email = models.EmailField(help_text="The contact email for the contributor.")
