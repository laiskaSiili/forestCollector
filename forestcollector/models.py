from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Other'),
    )

    name = models.CharField(default='', null=False, blank=False, max_length=10, help_text='Required')
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Required, must be between 0 and 100')
    profession = models.CharField(max_length=50, help_text='Who is reading a help text anyway?', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text='')


class Video(models.Model):
    name= models.CharField(max_length=500, null=False, blank=False)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="", validators=[FileExtensionValidator(['webm', 'mpg', 'ogg', 'mp4', 'm4p', 'm4v'])])

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class StandInformation(models.Model):
    ENTW = (
        ('JW', 'Jungwuchs'),
        ('SH', 'Stangenholz'),
        ('BH', 'Baumholz'),
        ('ST', 'Stufig')
    )

    lat = models.FloatField(blank=False, null=False, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    lon = models.FloatField(blank=False, null=False, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    accuracy = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0)])

    entwicklungsstufe = models.CharField(max_length=2, choices=ENTW, help_text='', blank=False, null=False)
    mischungsgrad = models.FloatField(blank=False, null=False, help_text='Mischungsgrad Nadelholz [0-100%]', default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    bemerkungen = models.TextField(blank=True, null=True, help_text='')