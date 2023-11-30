from django.contrib import admin
from .models import Book, Review, Tag

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Tag)


# @admin.register(Book, Review, Tag)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'created', 'status']
#     list_filter = ['status', 'created', 'author']
#     search_fields = ['title', 'body']

