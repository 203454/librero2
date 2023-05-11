from django.db import models

# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.CharField( max_length=10)
    editorial = models.CharField( max_length=250)
    ncapitulos = models.IntegerField()
    npaginas = models.IntegerField()
    isbn = models.IntegerField()
    actual = models.IntegerField()
    status = models.BooleanField()