from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'government.views.homepage'),
    (r'^government/$', 'government.views.year'),
    (r'^government/body/$', 'government.views.body'),
    (r'^government/body/name/$', 'government.views.name'),
    (r'^government/body/name/standing/$', 'government.views.standing'),
    (r'^admin/', include(admin.site.urls)),
)