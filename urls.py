from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.homepage'),
    (r'^government/(?P<year>[-\w]+)/$', 'government.views.year'),
    (r'^government/(?P<year>[-\w]+)/(?P<body>[-\w]+)/$', 'government.views.body'),
    (r'^government/(?P<year>[-\w]+)/(?P<body>[-\w]+)/(?P<name>[-\w]+)/$', 'people.views.person'),
    (r'^admin/', include(admin.site.urls)),
)

