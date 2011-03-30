from django.contrib import admin
from studentgov.people.models import Major, HousingType, GreekAffiliation, Hometown, Race


class MajorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class HousingTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'street_slug': ('street', ) }
    search_fields = ['street']

class GreekAffiliationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class HometownAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title', ) }
    search_fields = ['title']

admin.site.register(Major, MajorAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(GreekAffiliation, GreekAffiliationAdmin)
admin.site.register(Hometown, HometownAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Person)