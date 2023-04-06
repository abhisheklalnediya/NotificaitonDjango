from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from .models import Notifications


def index(request):
    success = False
    if request.method == 'POST':
        n = Notifications()
        n.title = request.POST.get('title', '')
        n.text = request.POST.get('text', '')
        n.image = request.FILES['image']
        n.name = request.POST.get('name', '')
        n.save()
        success = True
    nall = Notifications.objects.all()

    return render(request, 'index.html', {"success": success, "nall": nall})
