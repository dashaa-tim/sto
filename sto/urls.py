"""
Definition of urls for sto.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views
from django.shortcuts import render, redirect
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.views.generic import RedirectView

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Авторизация',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
        url(r'^links$', app.views.links, name='links'),
        url(r'^newpost$', app.views.newpost, name='newpost'),
        url(r'^registration$', app.views.registration, name='registration'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^blog$', app.views.blog, name='blog'),
        url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
        url(r'^anketa$', app.views.anketa, name='anketa'),
        url(r'^videopost$', app.views.videopost, name='videopost'),
        url(r'^services$', app.views.services, name='services'),
        url(r'^diagnost$', app.views.diagnost, name='diagnost'),
        url(r'^to$', app.views.to, name='to'),
        url(r'^dvs$', app.views.dvs, name='dvs'),
        url(r'^kompl$', app.views.kompl, name='kompl'),
        url(r'^torm$', app.views.torm, name='torm'),
        url(r'^ryl$', app.views.ryl, name='ryl'),
        url(r'^favicon\.ico$', RedirectView.as_view(url='/static/app/content/favicon.ico', permanent=True)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
