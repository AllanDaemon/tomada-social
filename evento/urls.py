from django.conf.urls import patterns, url
from views import EventoCreateView, EventoDetailView, EventoUpdateView, EventoDeleteView, EventoListView

urlpatterns = patterns('',
	url(r'^add/$', EventoCreateView.as_view(), name='evento-create'),
	url(r'^lista/$', EventoListView.as_view(), name='evento-list'),
	url(r'^(?P<pk>[\w\d]+)/$', EventoDetailView.as_view(), name='evento-detail'),
	url(r'^(?P<pk>[\w\d]+)/edit/$', EventoUpdateView.as_view(), name='evento-update'),
	url(r'^(?P<pk>[\w\d]+)/delete/$', EventoDeleteView.as_view(), name='evento-delete'),
)