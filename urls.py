from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('queue.views',
	url(r'^add$', 'add'),
	url(r'^remove$', 'remove'),
	url(r'^$', 'index'),
)

urlpatterns += staticfiles_urlpatterns()
