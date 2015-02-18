from django.shortcuts import render, render_to_response
from mongoengine.django.shortcuts import get_document_or_404

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core import serializers

import json

from mongoengine.queryset import Q
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Event, Account
from PIL import Image
import datetime

from lib.decorators import myuser_login_required

@myuser_login_required
def create(request):
    if request.method == 'POST':
        # save new evento
        title = request.POST['title']
        description = request.POST['description']
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        lat = request.POST['lat']
        lng = request.POST['lng']
        #image = request.FILES['image']

        event = Event(title=title)
        event.last_update = datetime.datetime.now()
        event.description = description
        event.date_start =  datetime.datetime.strptime(date_start, '%d/%m/%Y %H:%M')
        if not date_end:
            event.date_end = None
        else:
            event.date_end =  datetime.datetime.strptime(date_end, '%d/%m/%Y %H:%M')
        event.location =  [float(lat),float(lng)]
        user = request.session.get('userid')
        event.user = Account.objects(id=user)[0]
        #im = Image.open(image)
        #event.image.put(open(im))
        event.save()
        return HttpResponseRedirect(reverse('event-list'))

    return render_to_response('event/event_create.html',
                              context_instance=RequestContext(request))

@myuser_login_required
def list(request):
    # Get all events from DB
    id = request.session.get('userid')
    user = Account.objects(id=id)[0]
    events = Event.objects(user=user)
    return render_to_response('event/event_list.html', {'event_list': events},
                              context_instance=RequestContext(request))
@myuser_login_required
def search(request):
    # Get all events from DB
    lat = request.GET['lat']
    lng = request.GET['lng']
    radius = request.GET['radius']
    location = (float(lat),float(lng))
    date = request.GET['date'].ljust(10,'0')[0:10]
    date = datetime.datetime.fromtimestamp(int(date))
    events = Event.objects(
        Q(date_start__lte=date) & 
        (Q(date_end__gte=date) | Q(date_end__exists=False)) &
        Q(location__within_distance=[location, int(radius)])
        )
    # .values_list(
            # 'title', 
            # 'description', 
            # 'location',
            # 'date_start',
            # 'date_end')

    data = json.dumps( [{'id': str(e.id),
                           'title': e.title,
                           'description': e.description,
                           'location': e.location,
                           'date_start': str(e.date_start.strftime('%d/%m/%Y %H:%M')),
                           'date_end':  str(e.date_end.strftime('%d/%m/%Y %H:%M')) if e.date_end else ''} 
                        for e in events])

    return HttpResponse(data,content_type='application/json')

@myuser_login_required
def edit(request, event_id):
    event = get_document_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        # update field values and save to mongo
        title = request.POST['title']
        description = request.POST['description']
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        lat = request.POST['lat']
        lng = request.POST['lng']
        #image = request.FILES['image']

        event.title = title
        event.last_update = datetime.datetime.now()
        event.description = description
        event.date_start =  datetime.datetime.strptime(date_start, '%d/%m/%Y %H:%M')
        if not date_end:
            event.date_end = None
        else:
            event.date_end =  datetime.datetime.strptime(date_end, '%d/%m/%Y %H:%M')
        event.location =  [float(lat),float(lng)]
        user = request.session.get('userid')
        event.user = Account.objects(id=user)[0]
        #event.image = request.FILES['image']
        event.save()
        
        return HttpResponseRedirect(reverse('event-list'))

    elif request.method == 'GET':
        template = 'event/event_edit.html'
        if event.date_start:
            event.date_start = event.date_start.strftime('%d/%m/%Y %H:%M') 
        if event.date_end:
            event.date_end = event.date_end.strftime('%d/%m/%Y %H:%M')
        if event.location:
            event.lat = event.location[0]
            event.lng = event.location[1]
        params = {'event':event}
   
    return render_to_response(template, params, context_instance=RequestContext(request))

@myuser_login_required
def detail(request, event_id):
    event = get_document_or_404(Event, id=event_id)
    
    template = 'event/event_detail.html'
    if event.date_start:
        event.date_start = event.date_start.strftime('%d/%m/%Y %H:%M') 
    if event.date_end:
        event.date_end = event.date_end.strftime('%d/%m/%Y %H:%M')
    if event.location:
        event.lat = event.location[0]
        event.lng = event.location[1]
    params = {'event':event}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              
@myuser_login_required
def delete(request, event_id):
    event = get_document_or_404(Event, id=event_id)

    event.delete() 
    template = 'event/event_list.html'
    params = {'event_list': Event.objects} 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
@myuser_login_required
def home(request):
    return render_to_response('event/event_home.html',
                              context_instance=RequestContext(request))
                              
