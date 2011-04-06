from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def homepage(request):
    return HttpResponse("Welcome to the ASUN Tracker.")
    
def year(request):
    return HttpResponse("NVision 2010-2011.")
    
def body(request):
    return HttpResponse("Senate.")
    
def name(request):
    return HttpResponse("Andrew McClure.")
    
def standing(request):
    return HttpResponse("Senior.")