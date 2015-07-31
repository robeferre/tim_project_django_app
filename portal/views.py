from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django_tables2 import RequestConfig
from django.contrib.auth import logout
from portal.tables import *
from portal.models import *


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')



@login_required
def portal_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('portal/home.html', context_instance=RequestContext(request))



def projetos_main_page(request):
    """
    Pagina principal para listagem de projetos
    """
    queryset = Projetos.objects.select_related('nome_projeto','integrador','contend_provider','status','term_projeto').order_by('-nome_projeto')
    table = ProjetosMain(queryset)

    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render_to_response('portal/projetos_main.html', {'table': table}, context_instance=RequestContext(request))