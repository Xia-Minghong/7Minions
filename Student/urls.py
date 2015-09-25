from django.conf.urls import patterns, url
from Student import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^nice', views.nice, name='nice'),
    url(r'^home', views.home, name='home'),
)