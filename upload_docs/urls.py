from django.conf.urls import patterns, include, url
from upload_docs.views import *

urlpatterns = patterns('',

    #Url com a chave do projeto
    url(r'^([\w ]+)/$', list, name='list'),


)