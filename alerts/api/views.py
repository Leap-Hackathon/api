from django.shortcuts import render
from django.http import HttpResponse
from . import logic
import json
from .models import Wieght

def index(request):
    wieght_object = Wieght.objects.get(name = 'tea')
    progress = int((wieght_object.wieght/wieght_object.total_wieght)*100)
    # response_dict = {"progress":progress }
    # return HttpResponse(json.dumps(response_dict),content_type = "application/json")
    return HttpResponse(progress)

def save(request):
    wieght_input = request.GET.get("input") or ''
    wieght_object = Wieght.objects.get(name = 'tea')
    wieght_object.wieght = wieght_input
    wieght_object.save()
    response_dict = {"progress":'success' }
    return HttpResponse(json.dumps(response_dict),content_type = "application/json")
