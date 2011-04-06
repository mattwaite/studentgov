from people.models import BodyYear
from django.shortcuts import render_to_response

def homepage(request):
    bodyyears = BodyYear.objects.all()
    return render_to_response('homepage.html', {
        'bodyyears': bodyyears,
    })