# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings

# Create your models here.
class Missing(models.Model):
    nombre = models.CharField(max_length=50, blank=True)    
    primer_apellido = models.CharField(max_length=50, blank=True)
    segundo_apellido = models.CharField(max_length=50, blank=True)

    birthday_date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de nacimiento', help_text="Fecha de nacimiento",null=True, blank=True)
    TIPO_DE_IDENTIFICACION_OPT= (
        ('I', 'IFE'),
        ('P', 'PASAPORTE'),
        ('L', 'LICENCIA DE MANEJO'), 
        ('O', 'OTRO') 
    )
    TIPO_DE_IDENTIFICACION=models.CharField(max_length=2, choices= TIPO_DE_IDENTIFICACION_OPT,
                                            blank=True)
    num_de_identificacion= models.CharField(max_length=50, blank=True)
    
    SEXO_OPT= (
        ('M', 'Masculino'),
        ('F', 'Femenino'), 
    )
    sexo = models.CharField(max_length=2, choices= SEXO_OPT,blank=True)

    orientacion_sexual = models.CharField(max_length=50, blank=True)
    intervencion_quirurgica_modificar_sexo = models.CharField(max_length=50, blank=True)
    edad_aproximada=models.IntegerField()
    grupo_etnico = models.CharField(max_length=50, blank=True)
    migrante = models.CharField(max_length=50, blank=True)
    tiene_muestras_geneticas = models.CharField(max_length=2, blank=True)
    numero_referencia_de_muestra = models.CharField(max_length=50, blank=True)
    institucon_que_la_tomo = models.CharField(max_length=50, blank=True)
     
    def __str__(self):
        return self.nombre

class Origin(models.Model):
    missing_id = models.ForeignKey(Missing, verbose_name = "Desaparecido")
    nacionalidad=models.CharField(max_length=50, blank=True,default="Mexicano(a)")
    pais_origen=models.CharField(max_length=50, blank=True, default="México")
    colonia=models.CharField(max_length=100, blank=True) 
    calle=models.CharField(max_length=100, blank=True)
    numero=models.CharField(max_length=100, blank=True)
    current_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nacionalidad


class Physical_Description(models.Model):
    missing_id = models.ForeignKey(Missing, verbose_name = "Desaparecido")
    descripcion_fisica_desaparecido=models.CharField(max_length=300, blank=True)
    senias_particulares = models.CharField(max_length=300, blank=True)
    estatura=models.IntegerField()
    complexion= models.CharField(max_length=50, blank=True)
    tez=models.CharField(max_length=50, blank=True)
    tipo_de_cabello= models.CharField(max_length=50, blank=True)
    color_cabello= models.CharField(max_length=50, blank=True)
    color_de_ojos= models.CharField(max_length=50, blank=True)
    current_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.descripcion_fisica_desaparecido

class Found_Person(models.Model):
    missing_id = models.ForeignKey(Missing, verbose_name = "Desaparecido")
    date_found = models.DateTimeField(default=datetime.now, verbose_name='Fecha encontrado', help_text="Fecha encontrado",null=True, blank=True)
    status = models.IntegerField(default=1, max_length=2, blank=True)
    current_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.date_found

class Place_Missing(models.Model):
    missing_id = models.ForeignKey(Missing, verbose_name = "Desaparecido")
    fecha_desaparicion= models.DateTimeField(default=datetime.now, verbose_name='Fecha de desaparicion', help_text="Fecha de desaparicion",null=True, blank=True)
    SOLO_OPT= (
        ('0', 'Sólo'),
        ('1', 'Acompañado'), 
    )
    desaparicion_en_grupo = models.CharField(max_length=2,blank=True, 
                            verbose_name='Estaba sólo o acompañado', choices = SOLO_OPT)
    AVERIGUACION_OPT= (
        ('0', 'Sí'),
        ('1', 'No'), 
    )
    tiene_averiguacion_previa = models.CharField(max_length=2,blank=True, 
                                                choices=AVERIGUACION_OPT,
                                                help_text="Tiene averiguacion?")
    NUM_AVERIGUACION = models.CharField(max_length=100, blank=True)

    tipo_lugar_ultimavez_visto=models.CharField(max_length=100, blank=True)
    current_date = models.DateTimeField(auto_now=True)
    lat = models.TextField(max_length=250,blank=True)
    lng = models.TextField(max_length=250,blank=True)

    def __unicode__(self):
        return self.desaparicion_en_grupo