from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
from .forms_app import BookForm
from .models import Book, Review
objects = models.Manager()


def main_page(request):
    # главное меню приложения
    # return HttpResponse('Главная страница')
    return render(request, 'books/mainpage.html')


def about_page(request):
    # страница о приложении
    return render(request, 'books/about.html')


def contact_page(request):
    # страница контактов
    return render(request, 'books/contact.html')


def book_page(request, pk: str = 'введите название книги'):
    book_name = pk.capitalize()
    # страница о запрашиваемой книге
    return render(request, 'books/book.html', {'book_name': book_name})


def search_book(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = Book.objects.get(title=search_query)
        # book = Book.objects.filter(title=search_query)
    print('Search: ', search_query.title)

    # book = Book.objects.filter(title=search_query)
    context = {'book': 'book'}
    # print(book)
    return render(request, 'books/book_form.html', context)

    # if request.method == 'POST':
    #     name = request.POST['book_name']
    #     context = {'name': name}
    #     return render(request, 'books/book_form.html', context)
    # else:
    #     context = {'name': 'Название не указано'}
    #     return render(request, 'books/book_form.html', context)
    # return render(request, 'books/book_form.html')
    # search_query = ''

    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')
    #     book = Book.objects.filter



