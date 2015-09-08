from django.conf.urls import patterns, url
from Hello import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^nice', views.nice, name='nice'),
)