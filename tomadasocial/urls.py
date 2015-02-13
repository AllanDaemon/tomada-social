from django.conf.urls import patterns, include, url
from django.conf import settings
from evento.views import EventoHomeView

urlpatterns = patterns('',
    url(r'^$', 'event.views.home', name='event-home'),
    url(r'^evento/', include('evento.urls')),
	url(r'^conta/', include('conta.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^account/', include('account.urls'))
)

if settings.DEBUG:
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	urlpatterns += staticfiles_urlpatterns()

	urlpatterns += patterns('',
			url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
				'document_root': settings.MEDIA_ROOT,
			}),
	   )