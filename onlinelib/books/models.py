from django.db import models
import uuid
from django.db import models


class Book(models.Model):
    # создание колонок таблицы для описания объекта (книги)
    title = models.CharField(max_length=100)  # название книги
    description = models.TextField(null=True, blank=True)  # описание книги с флагом null=True (добавление книги без
    # описания)
    author = models.CharField(max_length=100)  # имя автора
    ISBN = models.CharField(max_length=100)  # номер ISBN
    tag = models.ManyToManyField('tag', blank=True)     # присвоение жанрового типа книге (возможно несколько жанров)
    vote_total = models.IntegerField(default=0, null=True, blank=True)  # суммарная оценка (по умолчанию равна 0)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)  # суммарная оценка (по умолчанию равна 0)
    created = models.DateTimeField(auto_now_add=True)  # дата создания записи
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)  # генерация id,
    objects = models.Manager()
    # уникальный, не редактируемый

    def __str__(self):
        return self.title


class Review(models.Model):
    # создание таблицы оценок книги пользователями приложения
    TYPE_VOTE = (
        ('+', 'Положительная оценка'),
        ('-', 'Отрицательная оценка'),
    )
    # owner =
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # получение id рецензируемой книги (удаление оценки
    # при удалении книги)
    bode = models.TextField(null=True, blank=True)  # описание рецензии
    value = models.CharField(max_length=100, choices=TYPE_VOTE)  # оценка книги
    created = models.DateTimeField(auto_now_add=True)  # дата создания записи
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    objects = models.Manager()
    def __str__(self):
        # возврат оценки при рецензии
        return self.value


class Tag(models.Model):
    # создание таблицы жанров
    genre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)  # дата создания записи
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    objects = models.Manager()
    def __str__(self):
        # возврат жанра
        return self.genre

