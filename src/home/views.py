from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    pageqs = PageVisit.objects.filter(path=request.path)
    context = {
        "title": "Saas",
        "welcome_msg": "hello there!",
        "page_visits": pageqs.count(),
        "total_visits": qs.count()
    }
    path = request.path
    PageVisit.objects.create(path=path)
    return render(request, 'home.html', context)