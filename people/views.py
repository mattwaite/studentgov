from people.models import Person, BodyYear, PersonYear
from government.models import Year, Body
from django.shortcuts import render_to_response

def year(request, year):
    personyears = PersonYear.objects.filter(body__year__slug=year).order_by('person__last_name')
    return render_to_response('people/year.html', {
        'personyears': personyears,
    })    

def person(request, name, pid):
    person = Person.objects.get(id=pid)
    personyears = PersonYear.objects.filter(person=person)
    return render_to_response('people/person.html', {
        'person': person,
        'personyears': personyears,
    })

