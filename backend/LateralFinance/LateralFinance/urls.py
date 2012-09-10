from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'api.views.home', name='home'),
    url(r'^quotes/?$', 'api.views.quotes', name='quotes'),
    url(r'^search/?$', 'api.views.autocomplete', name='autocomplete'),
    url(r'^admin/', include(admin.site.urls)),
)
