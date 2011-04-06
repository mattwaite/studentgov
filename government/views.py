from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from government.models import University, GovernmentName, Year, BodyType, Body
from people.models import BodyYear

    
def year(request, year):
    year = Year.objects.get(slug=year)
    governments = BodyYear.objects.filter(year=year)
    return render_to_response('government/year.html', {
        'governments': governments,
        'year': year,
})

#def body(request, year, body):
#    return HttpResponse(body)
#    
#def name(request, year, body, name):
#    return HttpResponse(name)
#    
#def standing(request):
#    return HttpResponse("Senior.")