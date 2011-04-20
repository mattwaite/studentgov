from people.models import BodyYear
from government.models import GovernmentName
from django.shortcuts import render_to_response

def homepage(request):
    govt = GovernmentName.objects.get(id=1)
    bodyyears = BodyYear.objects.all()
    return render_to_response('homepage.html', {
        'bodyyears': bodyyears,
        'govt': govt, 
    })