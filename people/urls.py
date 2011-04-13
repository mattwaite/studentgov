from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<year>[-\w]+)/$', 'people.views.year'),
    (r'^(?P<year>[-\w]+)/(?P<body_type>[-\w]+)/$', 'people.views.body_type'),
    (r'^(?P<year>[-\w]+)/(?P<body_type>[-\w]+)/(?P<body>[-\w]+)/$', 'people.views.body'),
    (r'^(?P<year>[-\w]+)/(?P<body_type>[-\w]+)/(?P<body>[-\w]+)/(?P<name>[-\w]+)/$', 'people.views.person'),
)