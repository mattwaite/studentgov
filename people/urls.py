from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', '.people.views.homepage'),
    (r'^$', 'people.views.body_type'),
    (r'^people/body_type(?P<body_type>[-\w]+)/$', 'people.views.body'),
    (r'^people/body_type/body/$', 'people.views.person'),
    (r'^admin/', include(admin.site.urls)),

)