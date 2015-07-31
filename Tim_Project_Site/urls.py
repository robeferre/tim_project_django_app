from django.conf.urls import patterns, include, url
from Tim_Project_Site import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Login / Logout
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'portal.views.logout_page'),

    # Web portal
    url(r'^portal/', include('portal.urls')),

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Ajax Functionality
    url(r'^ajax/', include('ajax.urls')),

)

# Serve static contend
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )