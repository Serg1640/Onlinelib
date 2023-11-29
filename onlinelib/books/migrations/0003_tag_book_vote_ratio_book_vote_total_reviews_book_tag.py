# Generated by Django 4.2.7 on 2023-11-28 21:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('genre', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('bode', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('+', 'Положительная оценка'), ('-', 'Отрицательная оценка')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(blank=True, to='books.tag'),
        ),
    ]