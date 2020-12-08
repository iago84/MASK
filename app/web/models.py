#!/usr/bin/python3
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import models
from enum import Enum
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.

class Noticias(models.Model):
    titulo=models.CharField('Titulo', max_length=100)
    cuerpo_noticia=models.TextField('Cuerpo',blank=True,null=True)
    link=models.URLField('Link',blank=True, null=True)
    def __str__(self):
        return self.titulo

class BlogEntry(models.Model):
    titulo=models.CharField('Titulo',max_length=200)
    imagen= models.ImageField('Imagen',upload_to='media',blank=True,null=True)
    linkV=EmbedVideoField(blank=True, null=True)
    date = models.DateField('Fecha', auto_now_add=None, blank=True, null=True)
    cuerpo_noticia=models.TextField('Cuerpo',blank=True,null=True)
    def __str__(self):
        return self.titulo


class Libros(models.Model):
    autor=models.CharField('Autor',max_length=60)
    titulo=models.CharField('Titulo',max_length=200)
    desc=models.TextField()
    type_libro={'Poesia':'Poesia','Relato corto':'Relato corto','Comic':'Comic'}
    tipolib= models.CharField('Tipo de Libro',max_length=30,choices=type_libro.items())
    portada=models.ImageField('Portada')
    text=models.FileField('Texto del libro',blank=True,null=True)

    url=models.URLField('Url',blank=True,null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('LibroDetail',args=[self.id])

    def leer(self):
        return reverse('Leer',args=[self.id])



class Visita(models.Model):
    nombre=models.CharField('nombre',max_length=100)
    comentario=models.TextField('comentario')
    def __str__(self):
        return self.nombre





# Create your models here.
class auction(models.Model):
    LIFECYCLES_ = (
        ('A', 'Active'),
        ('B', 'Banned'),
        ('D', 'Due'),
        ('X', 'Adjudicated'),
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    min_price = models.FloatField()
    deadline = models.DateTimeField()
    lifecycle = models.CharField(max_length=1, choices=LIFECYCLES_)

    lock = models.BooleanField(default=False)
    #imagen=models.ImageField('Imagen',upload_to='media')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['deadline']


class bid(models.Model):

    STATUS_ = (
        ('W', 'Wining'),
        ('L', 'Losing'),
    )

    auct = models.ForeignKey(auction, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_)