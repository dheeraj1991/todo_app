from django.conf.urls import patterns, url
from task.views import Task_Page

urlpatterns = patterns('',
       url(r'^home/', Task_Page.as_view(), name='task'),
       url(r'^update/', 'task.views.task_update', name='update'),
       url(r'^delete/', 'task.views.task_delete', name='delete'),
)