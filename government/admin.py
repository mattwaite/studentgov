from django.contrib import admin
from studentgov.government.models import University, GovernmentName, Year, BodyType

class UniversityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']
    pass

class GovernmentNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']
    pass

class Yeardmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']
    pass

class BodyTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']
    pass

admin.site.register(University, UniversityAdmin)
admin.site.register(GovernmentName, GovernmentNameAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(BodyType, BodyTypeAdmin)