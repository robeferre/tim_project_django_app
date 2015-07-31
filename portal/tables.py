import django_tables2 as tables


##################################
#  Tabela principal de projetos  #
##################################

TEMPLATE = '''

   <a href="{% url list record.nome_projeto %}" class="docs_button" title="Docs" ><img src="/static_media/images/project_screen/doc-icon.png" class="png"/></a>

'''

class ProjetosMain(tables.Table):

    #pdb.set_trace()
    nome_projeto = tables.Column(verbose_name='Projeto',orderable=False)

    #nome_projeto = tables.Column()
    integrador = tables.Column(verbose_name='Integrador',orderable=False)
    contend_provider = tables.Column(verbose_name='Content Provider',orderable=False)
    status = tables.Column(verbose_name='Status',orderable=False)
    term_projeto = tables.Column(verbose_name='Vigencia',orderable=False)
    acoes =  tables.TemplateColumn(TEMPLATE)

    class Meta:
        orderable = False
        attrs = {'class': 'paleblue'}




