from django.conf.urls import patterns, url
from views import ContaCreateView, ContaListView, ContaDetailView, ContaUpdateView, ContaDeleteView, ContaLoginView 

urlpatterns = patterns('',
	url(r'^add/$', ContaCreateView.as_view(), name='conta-create'),
	url(r'^lista/$', ContaListView.as_view(), name='conta-list'),
	url(r'^login/$', ContaLoginView.as_view(), name='conta-login'),
	url(r'^(?P<pk>[\w\d]+)/$', ContaDetailView.as_view(), name='conta-detail'),	
	url(r'^(?P<pk>[\w\d]+)/edit/$', ContaUpdateView.as_view(), name='conta-update'),
	url(r'^(?P<pk>[\w\d]+)/delete/$', ContaDeleteView.as_view(), name='conta-delete'),
)