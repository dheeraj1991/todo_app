from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^user/', include('authentication.urls', namespace='user')),
    url(r'^admin/', include(admin.site.urls)),
)
