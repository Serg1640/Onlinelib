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


def book_page(request, pk: str):
    book_name = pk.capitalize()
    return render(request, 'books/book.html', {'book_name': book_name})


def search_book(request):
    # функция поиска книги по БД
    book, book_title, book_author = '', '', ''      # значения описания книги по умолчанию
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        # проверка наличия книги в БД
        if Book.objects.filter(title=search_query).exists():
            print('Есть инфа в БД')
            book = Book.objects.filter(title=search_query)
        else:
            print('Записи нет')
            book = 'Книги нет'
            contex = {'book': book}
            return render(request, 'books/book_form.html', contex)
        book = Book.objects.filter(title=search_query)
    for b in book:
        book_title = b.title
        book_author = b.author
        # print(b.author)
    print('Вы ищите', book)
    contex = {'book': book, 'book_title': book_title, 'book_author': book_author}
    return render(request, 'books/book_form.html', contex)






