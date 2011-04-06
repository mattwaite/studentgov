from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^(?P<year>[-\w]+)/$', 'government.views.year'),
    (r'^(?P<year>[-\w]+)/(?P<body>[-\w]+)/$', 'government.views.body'),
    (r'^(?P<year>[-\w]+)/(?P<body>[-\w]+)/(?P<name>[-\w]+)/$', 'government.views.name'),
    (r'^(?P<year>[-\w]+)/(?P<body>[-\w]+)/(?P<name>[-\w]+)/(?P<standing>[-\w]+)/$', 'government.views.standing'),
)