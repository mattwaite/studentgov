from django.contrib import admin
from studentgov.people.models import Major, HousingType, GreekAffiliation, Hometown, Race, Person

class MajorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'major_slug': ('major', ) }

class HousingTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'housing_type_slug': ('housing_type', ) }

class GreekAffiliationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'greek_affiliation_slug': ('greek_affiliation', ) }

class HometownAdmin(admin.ModelAdmin):
    prepopulated_fields = {'hometown_slug': ('hometown', ) }
    search_fields = ['name']

class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'race_slug': ('race', ) }

admin.site.register(Major, MajorAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(GreekAffiliation, GreekAffiliationAdmin)
admin.site.register(Hometown, HometownAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Person)