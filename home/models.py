from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Telefon(models.Model):
    nomi = models.CharField(max_length=255)
    rangi = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


##################################################################################################################

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/Slider',
                              validators=[FileExtensionValidator(allowed_extensions={'jpg', 'jpeg', 'png', })])

    def __str__(self):
        return self.title


#################################################################################################################

class News(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    rich_text = RichTextUploadingField()

    def str(self):
        return self.title


######################################################################################################################

class Phone(models.Model):
    title = models.CharField(max_length=300)
    number = models.IntegerField()
    dscrb = models.TextField()

    def str(self):
        return self.title
