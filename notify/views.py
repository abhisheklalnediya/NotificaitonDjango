from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from .models import Notifications


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def add(request):
    n = Notifications()
    n.title = request.POST.get('title', '')
    n.text = request.POST.get('text', '')
    n.image = request.POST.get('image', '')
    n.name = request.POST.get('name', '')
    n.save()
    template = loader.get_template('added.html')
    return HttpResponse(template.render())
