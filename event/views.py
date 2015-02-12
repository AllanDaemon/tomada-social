from django.shortcuts import render, render_to_response
from mongoengine.django.shortcuts import get_document_or_404

from django.template import RequestContext
from models import Event
import datetime

from lib.decorators import myuser_login_required

@myuser_login_required
def create(request):
    if request.method == 'POST':
        # save new evento
        title = request.POST['title']
        description = request.POST['description']

        event = Event(title=title)
        event.last_update = datetime.datetime.now()
        event.description = description
        event.save()

    return render_to_response('event/event_create.html',
                              context_instance=RequestContext(request))

@myuser_login_required
def list(request):
    # Get all events from DB
    events = Event.objects
    return render_to_response('event/event_list.html', {'event_list': events},
                              context_instance=RequestContext(request))

@myuser_login_required
def edit(request, event_id):
    event = get_document_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        # update field values and save to mongo
        event.title = request.POST['title']
        event.last_update = datetime.datetime.now() 
        event.description = request.POST['description']
        #event.location = request.POST['location']
        event.save()
        template = 'event/event_list.html'
        params = {'event_list': Event.objects} 

    elif request.method == 'GET':
        template = 'event/event_edit.html'
        params = {'event':event}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              
@myuser_login_required
def delete(request, event_id):
    event = get_document_or_404(Event, id=event_id)

    event.delete() 
    template = 'event/event_list.html'
    params = {'event_list': Event.objects} 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
    