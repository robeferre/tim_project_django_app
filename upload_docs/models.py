# -*- coding: utf-8 -*-
from django.db import models
from portal.models import Projetos
import portal

# Create your models here.
class Document(models.Model):

    docfile = models.FileField(upload_to="documents/%Y/%m/%d")
    user = models.CharField("Usuario ",max_length=50)
    file_name = models.CharField("Nome",max_length=150)
    data_upload = models.DateTimeField("Anexado em")

    #FOREIGN KEY "Projetos"
    projetos = models.ForeignKey(portal.models.Projetos)


    def __unicode__(self):
        return self.file_name

