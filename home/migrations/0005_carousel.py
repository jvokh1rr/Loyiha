# Generated by Django 4.2.7 on 2023-11-16 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_phone_notebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/Slider', validators=[django.core.validators.FileExtensionValidator(allowed_extensions={'jpg', 'jpeg', 'png'})])),
            ],
        ),
    ]