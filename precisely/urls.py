from django.conf.urls import patterns, include, url
from precisely import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('sign_pdf.views',
    url(r'^$', 'home', name='home'),
    url(r'^signed/$', 'signed', name='signed'),
    url(r'^sign/$', 'send_to_sign', name='sign'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
