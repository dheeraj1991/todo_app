from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^user/', include('authentication.urls', namespace='user')),
    url(r'^task/', include('task.urls', namespace='tasks')),
    url(r'^admin/', include(admin.site.urls)),
)
