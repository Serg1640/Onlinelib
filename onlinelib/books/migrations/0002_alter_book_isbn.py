# Generated by Django 4.2.7 on 2023-11-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=100),
        ),
    ]
