from django.db import models

class University(models.Model):
    full_name = models.CharField(max_length=255)
    abbrev = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)
    def __unicode__(self):
        return self.full_name
    
class GovernmentName(models.Model):
    full_name = models.CharField(max_length=255)
    slug = models.SlugField()
    abbrev = models.CharField(max_length=20)
    university = models.ForeignKey(University)
    url = models.URLField(verify_exists=True)
    email_address = models.EmailField(max_length=255, blank=True, null=True)
    date_founded = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.full_name

class Year(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.title
    
class BodyType(models.Model):
    body_type = models.CharField(max_length=255)
    slug = models.SlugField()
    def __unicode__(self):
        return self.body_type

class Body(models.Model):
    government = models.ForeignKey(GovernmentName)
    body_type = models.ForeignKey(BodyType)
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    year = models.ForeignKey(Year)
    description = models.TextField(blank=True, null=True)
    main_governing_body = models.BooleanField()
    def __unicode__(self):
        return self.name