from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jarrett.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
