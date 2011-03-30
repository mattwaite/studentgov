from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^people/', include(studentgov.people.urls)),
    (r'^government/', include(studentgov.government.urls)),    
    (r'^admin/', include(admin.site.urls)),
)

