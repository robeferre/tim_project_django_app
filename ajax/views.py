# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from upload_docs.models import Document
from django.views.decorators.csrf import csrf_exempt
from upload_docs.models import Document
from django.core.files.storage import default_storage
import pdb


@csrf_exempt
def ajax_delete_doc(request):

    # Delete docs
    if request.is_ajax():
        if request.method == 'POST':

            #Deleting file from DB and File System
            file_id = request.POST.getlist('id')[0]
            doc = Document.objects.get(id=file_id)

            if doc.user == request.user.first_name:
                default_storage.delete(doc.docfile)
                doc.delete()
                success='true'
                return HttpResponse(success)
            else:
                success='false'
                return HttpResponse(success)




