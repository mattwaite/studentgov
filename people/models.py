from django.db import models
from government.models import Body, Year

class Major(models.Model):
    major = models.CharField(max_length=255)
    major_slug = models.SlugField()
    def __unicode__(self):
        return self.major
    
class HousingType(models.Model):
    housing_type = models.CharField(max_length=255)
    housing_type_slug = models.SlugField()
    def __unicode__(self):
        return self.housing_type

class GreekAffiliation(models.Model):
    greek_affiliation = models.CharField(max_length=255)
    greek_affiliation_slug = models.SlugField()
    def __unicode__(self):
        return self.greek_affiliation

class Hometown(models.Model):
    hometown = models.CharField(max_length=255)
    hometown_slug = models.SlugField()
    def __unicode__(self):
        return self.hometown
    
class Race(models.Model):
    race = models.CharField(max_length=255)
    race_slug = models.SlugField()
    def __unicode__(self):
        return self.race
    
class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    name_slug = models.SlugField()
    hometown = models.ForeignKey(Hometown, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True, null=True)
    race = models.ForeignKey(Race, blank=True, null=True)
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class PersonYear(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )
    person = models.ForeignKey(Person)
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    major = models.ManyToManyField(Major, blank=True, null=True)
    housing_type = models.ForeignKey(HousingType, blank=True, null=True)
    greek = models.BooleanField()
    greek_affiliation = models.ManyToManyField(GreekAffiliation, blank=True, null=True)
    def __unicode__(self):
        return "%s %s" % (self.person, self.year)

class BodyYear(models.Model):
    year = models.ForeignKey(Year)
    body = models.ForeignKey(Body)
    members = models.ManyToManyField(PersonYear)
    def __unicode__(self):
        return "%s %s" % (self.year, self.body)