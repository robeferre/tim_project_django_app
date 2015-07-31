from portal.models import Projetos
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
import pdb

##################################
#  Tabela principal de projetos  #
##################################

TEMPLATE = '''{% load filename %}
  <a href=" {{ record.docfile.url }} "> {{ record.docfile.name|filename  }} </a>
'''

TEMPLATE_DEL = '''

    {% csrf_token %}
  <button id ="{{record.pk}}" class="remove-button">Remover</button>

'''

class UploadedFiles(tables.Table):
    docfile = tables.TemplateColumn(TEMPLATE,verbose_name="Nome do arquivo")

    data_upload = tables.Column(verbose_name='Data de upload',orderable=True)
    user = tables.Column(verbose_name='Usuario',orderable=False)
    acoes =  tables.TemplateColumn(TEMPLATE_DEL)

    class Meta:
        orderable = False
        attrs = {'class': 'paleblue'}