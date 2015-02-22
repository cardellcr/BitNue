from django.http import HttpResponseRedirect, HttpResponse
from web.models import *
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone


def index(request):
  #events = Event.objects.filter(start_date__day = timezone.now().day)
  #date = timezone.now()
  context = {'events': 'events', 'date': 'date'}

  return render_to_response("index.html", context)
