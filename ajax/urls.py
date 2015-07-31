from django.conf.urls import patterns, include, url

urlpatterns = patterns('ajax.views',
    url(r'delete_doc/$',
        view='ajax_delete_doc',
        name='ajax_delete_doc'),
)