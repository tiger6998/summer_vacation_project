from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'movie_night.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/', include('movies.urls')),
    url(r'^people/', include('people.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )