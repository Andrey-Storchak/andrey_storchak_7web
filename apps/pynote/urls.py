from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.conf import settings

from apps.pynote import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^/add$', views.AddNoteView.as_view(), name='add_note'),
)

