from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.homepage'),
    (r'^government/(?P<year>[-\w]+)/$', 'government.views.year'),
    (r'^government/(?P<year>[-\w]+)/(?P<body>[-\w]+)/$', 'government.views.body'),
    (r'^people/by-year/(?P<year>[-\w]+)/$', 'people.views.year'),
    (r'^people/details/(?P<name>[-\w]+)/(?P<pid>[-\w]+)/$', 'people.views.person'),
    (r'^admin/', include(admin.site.urls)),
)

