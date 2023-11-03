__author__ = "Deepak Verma"

import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)

class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Date Updatd"), auto_now=True, db_index=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Date Updatd"), auto_now=True, db_index=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    books = models.ManyToManyField(Book, related_name="categories")
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Date Updatd"), auto_now=True, db_index=True)

    # book = Book.objects.get(pk=1)
    # categories = book.categories.all()
    # categories is a reverse relationship

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_sold = models.PositiveIntegerField()

    created_at = models.DateTimeField(_("Sale Date"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Date Updatd"), auto_now=True, db_index=True)
