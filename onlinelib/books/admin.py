from django.contrib import admin
from .models import Book, Review, Tag

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Tag)


# Register your models here.
