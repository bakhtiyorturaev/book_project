# Generated by Django 5.0.1 on 2024-01-21 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='authors_table',
        ),
        migrations.AlterModelTable(
            name='bookauthor',
            table='book_author_table',
        ),
        migrations.AlterModelTable(
            name='bookreview',
            table='review_table',
        ),
        migrations.AlterModelTable(
            name='books',
            table='books_table',
        ),
    ]
