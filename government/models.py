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
    url = models.URLField(verify_exists)
    email_address = models.EmailField(max_length=255, blank=True, null=True)
    date_founded = models.CharField(blank=True, null=True)
    def __unicode__(self):
        return self.full_name

class Year(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    start_date = models.DateField
    end_date = models.DateField
    def __unicode__(self):
        return self.title
    
class BodyType(models.Model):
    body_type = models.CharField(max_length=255)
    slug = models.SlugField()
    def __unicode__(self):
        return self.body_type
