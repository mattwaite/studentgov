from people.models import Person, BodyYear
from government.models import Year
from django.shortcuts import render_to_response

def year(request, year):
    year = Year.objects.get(slug=year)
    govtyear = BodyYear.objects.filter(year=year)
    return render_to_response('people/year.html', {
        'govtyear': govtyear,
        'year': year,
    })

