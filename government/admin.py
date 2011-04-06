from django.contrib import admin
from studentgov.government.models import University, GovernmentName, Year, BodyType, Body
    
class GovernmentNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('full_name',) }
    
class YearAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',) }
    
class BodyTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('body_type',) }

class BodyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name',) }

admin.site.register(University)
admin.site.register(GovernmentName, GovernmentNameAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(BodyType, BodyTypeAdmin)
admin.site.register(Body, BodyAdmin)