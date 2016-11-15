#encoding:utf-8
import logging
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

logger = logging.getLogger(__name__)

class Fossas(models.Model):
    user = models.ForeignKey(User, verbose_name = "Usuario")
    reference = models.CharField(verbose_name = "Referencia Topografica", max_length=250)
    datas = models.CharField(verbose_name = "Datos", max_length=250)
    bodys = models.IntegerField(verbose_name='Cuerpos', blank=True)
    fossa = models.IntegerField(verbose_name='Fosas', blank=True)
    current_date = models.DateTimeField(auto_now=True)
    inumation_date = models.DateField(default=datetime.now, verbose_name='Fecha de inhumación', help_text="Fecha de inhumación",null=True, blank=True)
    exumation_date= models.DateTimeField(default=datetime.now, verbose_name='Fecha de exhumación', help_text="Fecha de inhumación",null=True, blank=True)
    discovery_date= models.DateTimeField(default=datetime.now, verbose_name='Fecha de Descubrimiento', help_text="Fecha de Descubrimiento",null=True, blank=True)
    description = models.TextField(verbose_name='Observaciones', max_length=250)
    address = models.TextField(verbose_name='Direccion', max_length=250, blank=True)
    lat = models.TextField(max_length=250,blank=True)
    lng = models.TextField(max_length=250,blank=True)

    def __unicode__(self):
        return self.reference
