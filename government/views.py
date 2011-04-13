from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from government.models import University, GovernmentName, Year, BodyType, Body
from people.models import PersonYear

    
def year(request, year):
    yr = Year.objects.get(slug=year)
    governments = Body.objects.filter(year=yr)
    return render_to_response('government/year.html', {
        'governments': governments,
        'year': year,
})

def body(request, year, body):
    yr = Year.objects.get(slug=year)
    government = Body.objects.get(year=yr, name_slug=body)
    person_year = PersonYear.objects.filter(body__year__slug=year, body=government)
    return render_to_response('government/body.html', {
        'year': year,
        'government': government,
        'person_year': person_year,
})
    
    
#def name(request, year, body, name):
    
    
#def standing(request):
    