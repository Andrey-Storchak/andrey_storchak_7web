from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import apps.pynote.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include(apps.pynote.urls)),
    url(r'^index$', include(apps.pynote.urls)),
    url(r'^notes', include(apps.pynote.urls)),
    url(r'^admin/', include(admin.site.urls)),
    )

urlpatterns += patterns('',
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
)
urlpatterns += patterns('',
    url(r'media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)
