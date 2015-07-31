# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from upload_docs.models import Document
from upload_docs.forms import DocumentForm
from upload_docs.tables import *
from portal.models import Projetos
import datetime

def list(request, nome_projeto):


    e = Projetos.objects.get(nome_projeto=nome_projeto)
    pk=e.id



    # Handle file upload
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():

            newdoc = Document(

                docfile=request.FILES['docfile'],
                user = request.user.first_name,
                data_upload=datetime.datetime.now(),
                projetos_id = pk,
                file_name=request.FILES['docfile'].name

            )
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse("upload_docs.views.list", args=[nome_projeto]))
    else:
        form = DocumentForm() # A empty, unbound form



    # Load documents for the list page
    documents = Document.objects.filter(projetos_id=int(pk))
    queryset = documents.select_related('docfile','data_upload','user').order_by('-data_upload')
    table = UploadedFiles(queryset)
    table.paginate(page=request.GET.get('page', 1), per_page=10)

    # Render list page with the documents and the form
    return render_to_response('file_upload/file_upload_new.html',
            {'table': table, 'form': form,'nome_projeto': nome_projeto,},
        context_instance=RequestContext(request)
    )