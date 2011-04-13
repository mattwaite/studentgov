from people.models import Person, BodyYear, PersonYear
from government.models import Year, Body
from django.shortcuts import render_to_response

def person(request, year, body, name):
    yr = Year.objects.get(slug=year)
    government = Body.objects.get(year=yr, name_slug=body)
    person = PersonYear.objects.get(body__year__slug=year, body=government, person__name_slug=name)
    return render_to_response('people/person.html', {
        'yr': yr,
        'government': government,
        'person': person,
    })

