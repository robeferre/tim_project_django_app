from django.conf.urls import *
from portal.views import *



urlpatterns = patterns('',

    # Main Page portal / HOME page
    url(r'^$', portal_main_page),

    # Project Page
    url(r'^projetos/$', projetos_main_page),

    # Upload Docs / Projetos
    url(r'^projetos/docs/', include('upload_docs.urls')),

)