from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import apps.pynote.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'andrey_storchak_test_7web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(apps.pynote.urls)),

)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        )
