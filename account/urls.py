from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^create/$', 'account.views.create', name='account-create'),
	url(r'^list/$', 'account.views.list', name='account-list'),
	url(r'^login/$', 'account.views.login', name='account-login'),
	url(r'^(?P<account_id>[\w\d]+)/edit/$', 'account.views.edit', name='account-edit'),
	url(r'^(?P<account_id>[\w\d]+)/delete/$', 'account.views.delete', name='account-delete'),
)