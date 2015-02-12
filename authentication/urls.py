from django.conf.urls import patterns, url
from authentication.views import SignUp, Login

urlpatterns = patterns('',
       url(r'^signup/', SignUp.as_view(), name='signup'),
       url(r'^login/', Login.as_view(), name='signup'),
       url(r'logout/', 'authentication.views.user_logout', name='user_logout'),
)