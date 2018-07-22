""" Default urlconf for freefolks """

from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = [
	# Examples:
    # url(r'^$', 'freefolks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^backoffice/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^bad/$', bad),
    url(r'', include('base.urls')),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns +=(
    	url(r'^__debug__/', include(debug_toolbar.urls)),
    )
