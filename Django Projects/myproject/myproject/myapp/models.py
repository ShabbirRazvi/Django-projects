from django.db import models
from django.urls import reverse

# Create your models here.


class Books_model(models.Model):
    book_name = models.CharField(max_length=30)
    book_id = models.IntegerField()
    book_auth = models.CharField(max_length=30)
    book_copies = models.IntegerField()

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse()

