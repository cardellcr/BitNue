from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^services', views.services, name='services'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
)
