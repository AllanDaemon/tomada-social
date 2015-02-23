from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^create/$', 'event.views.create', name='event-create'),
	url(r'^list/$', 'event.views.list', name='event-list'),
	url(r'^going/$', 'event.views.eventGoing', name='event-going'),
	url(r'^search/$', 'event.views.search', name='event-search'),
	url(r'^(?P<event_id>[\w\d]+)/edit/$', 'event.views.edit', name='event-edit'),
	url(r'^(?P<event_id>[\w\d]+)/delete/$', 'event.views.delete', name='event-delete'),
	url(r'^(?P<event_id>[\w\d]+)/detail/$', 'event.views.detail', name='event-detail'),
	url(r'^(?P<event_id>[\w\d]+)/join/$', 'event.views.join', name='event-join'),
)