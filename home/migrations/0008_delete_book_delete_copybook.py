# Generated by Django 4.2.7 on 2023-11-16 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_book_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Copybook',
        ),
    ]
