from django.db import models
from django import forms


class BookForm(forms.Form):
    name = models.CharField(max_length=100)
