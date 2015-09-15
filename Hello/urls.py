from django.conf.urls import patterns, url
from Hello.views import *
#from Hello import views

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^nice', nice, name='nice'),
    url(r'^home', home, name='home'),
)