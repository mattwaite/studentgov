from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^(?P<year>[-\w]+)/$', '.people.views.year'),
    (r'^(?P<year>[-\w]+)/(?P<body>[-\w]+)/$', 'people.views.body_type'),
    (r'^(?P<year>[-\w]+)/(?P<body>[-\w]+)/$', 'people.views.body'),
    (r'^(?P<year>[-\w]+)/(?P<body>[-\w]+)/$$', 'people.views.person'),
    (r'^admin/', include(admin.site.urls)),

)