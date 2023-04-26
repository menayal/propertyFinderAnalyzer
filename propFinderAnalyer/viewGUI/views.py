from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, "index.html")
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, "viewGUI/index.html", context)

    # Create your views here.
